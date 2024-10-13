def middle_column_score(v, w, match, mismatch, indel):
    '''Returns the score of the middle column for the alignment of v and w.'''

    # Initialize the score columns.
    S = [[i * j * indel for j in range(-1, 1)] for i in range(len(v)+1)]
    S[0][1] = -indel
    backtrack = [0] * (len(v) + 1)

    # Fill in the Score and Backtrack matrices.
    for j in range(1, len(w)//2 + 1):
        for i in range(0, len(v) + 1):
            if i == 0:
                S[i][1] = -j * indel
            else:
                score_match = match if v[i-1] == w[j-1] else -mismatch
                scores = [
                    S[i-1][0] + score_match,  # match/mismatch
                    S[i][0] - indel,          # insertion (gap in v)
                    S[i-1][1] - indel          # deletion (gap in w)
                ]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)//2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def middle_edge(v, w, match, mismatch, indel):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle. Backtrack is unnecessary here.
    source_to_middle = middle_column_score(v, w, match, mismatch, indel)[0]

    # Get the score of the middle column from the middle to the sink. Reverse the sequences and backtrack.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1] + ['$', ''][len(w) % 2 == 1 and len(w) > 1], match, mismatch, indel))

    # Get the component-wise sum of the middle column scores.
    scores = list(map(sum, zip(source_to_middle, middle_to_sink)))

    # Get the position of the maximum score and determine the next node.
    max_middle = max(range(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)//2 + 1)
    else:
        next_node = [
            (max_middle + 1, len(w)//2 + 1),
            (max_middle, len(w)//2 + 1),
            (max_middle + 1, len(w)//2),
        ][backtrack[max_middle]]

    return (max_middle, len(w)//2), next_node


if __name__ == '__main__':
    # Input
    match = 1      # Reward for a match
    mismatch = 1   # Penalty for a mismatch
    indel = 5      # Penalty for an indel (gap)

    # Example input
    v = ""
    w = ""

    # Get the middle edge.
    middle = middle_edge(v, w, match, mismatch, indel)

    # Print the result
    print('Middle Edge:', middle)
