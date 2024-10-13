def global_alignment(v, w, match, mismatch, indel):
    # Initialize the DP table
    n, m = len(v), len(w)
    score = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize first row and column with indel penalties
    for i in range(1, n + 1):
        score[i][0] = score[i - 1][0] - indel
    for j in range(1, m + 1):
        score[0][j] = score[0][j - 1] - indel

    # Fill in the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_mismatch = match if v[i - 1] == w[j - 1] else -mismatch
            score[i][j] = max(score[i - 1][j - 1] + match_mismatch,  # match/mismatch
                              score[i - 1][j] - indel,              # indel in w
                              score[i][j - 1] - indel)              # indel in v

    # Traceback to get the alignment
    i, j = n, m
    aligned_v, aligned_w = [], []
    
    while i > 0 and j > 0:
        match_mismatch = match if v[i - 1] == w[j - 1] else -mismatch
        if score[i][j] == score[i - 1][j - 1] + match_mismatch:
            aligned_v.append(v[i - 1])
            aligned_w.append(w[j - 1])
            i -= 1
            j -= 1
        elif score[i][j] == score[i - 1][j] - indel:
            aligned_v.append(v[i - 1])
            aligned_w.append('-')
            i -= 1
        else:
            aligned_v.append('-')
            aligned_w.append(w[j - 1])
            j -= 1

    # If one of the strings is not fully traversed, add gaps
    while i > 0:
        aligned_v.append(v[i - 1])
        aligned_w.append('-')
        i -= 1
    while j > 0:
        aligned_v.append('-')
        aligned_w.append(w[j - 1])
        j -= 1

    # Reverse to get the correct order
    aligned_v = ''.join(aligned_v[::-1])
    aligned_w = ''.join(aligned_w[::-1])

    # Return the score and the alignment
    return score[n][m], aligned_v, aligned_w


# Sample Input
with open("input.txt", "r") as f:
    match, mismatch, indel = map(int, f.readline().split())
    v = f.readline().strip()
    w = f.readline().strip()

# Compute alignment
score, aligned_v, aligned_w = global_alignment(v, w, match, mismatch, indel)

# Output the result
print(score)
print(aligned_v)
print(aligned_w)
