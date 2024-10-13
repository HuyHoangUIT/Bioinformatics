from math import inf

def AffineGapPenalties(v, w, match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty):
    lv = len(v)
    lw = len(w)

    # Initialize score matrices
    lower_scores_matrix = [[0] * (lw+1) for _ in range(lv+1)]
    middle_scores_matrix = [[0] * (lw+1) for _ in range(lv+1)]
    upper_scores_matrix = [[0] * (lw+1) for _ in range(lv+1)]

    # Initialize backtrack matrices
    lower_backtrack_matrix = [[0] * (lw+1) for _ in range(lv+1)]
    middle_backtrack_matrix = [[0] * (lw+1) for _ in range(lv+1)]
    upper_backtrack_matrix = [[0] * (lw+1) for _ in range(lv+1)]

    # Initialize base cases
    for i in range(1, lv+1):
        upper_scores_matrix[i][0] = -inf
        middle_scores_matrix[i][0] = -gap_opening_penalty - (gap_extension_penalty * (i - 1))
        lower_scores_matrix[i][0] = -gap_opening_penalty - (gap_extension_penalty * (i - 1))
        upper_backtrack_matrix[i][0] = v[i-1]
        middle_backtrack_matrix[i][0] = v[i-1]
        lower_backtrack_matrix[i][0] = v[i-1]

    for j in range(1, lw+1):
        upper_scores_matrix[0][j] = -gap_opening_penalty - (gap_extension_penalty * (j - 1))
        middle_scores_matrix[0][j] = -gap_opening_penalty - (gap_extension_penalty * (j - 1))
        lower_scores_matrix[0][j] = -inf
        upper_backtrack_matrix[0][j] = w[j-1]
        middle_backtrack_matrix[0][j] = w[j-1]
        lower_backtrack_matrix[0][j] = w[j-1]

    # Fill matrices
    for i in range(1, lv+1):
        for j in range(1, lw+1):
            if v[i-1] == w[j-1]:
                score = match_reward
            else:
                score = -mismatch_penalty

            lower_im1_j = lower_scores_matrix[i-1][j]
            middle_im1_j = middle_scores_matrix[i-1][j]
            upper_i_jm1 = upper_scores_matrix[i][j-1]
            middle_i_jm1 = middle_scores_matrix[i][j-1]
            middle_im1_jm1 = middle_scores_matrix[i-1][j-1]

            lower_scores_matrix[i][j] = max(lower_im1_j - gap_extension_penalty, middle_im1_j - gap_opening_penalty)
            lower_backtrack_matrix[i][j] = "-"
            if lower_scores_matrix[i][j] == middle_im1_j - gap_opening_penalty:
                lower_backtrack_matrix[i][j] = "M"

            upper_scores_matrix[i][j] = max(upper_i_jm1 - gap_extension_penalty, middle_i_jm1 - gap_opening_penalty)
            upper_backtrack_matrix[i][j] = "|"
            if upper_scores_matrix[i][j] == middle_i_jm1 - gap_opening_penalty:
                upper_backtrack_matrix[i][j] = "M"

            middle_scores_matrix[i][j] = max(
                upper_scores_matrix[i][j], middle_im1_jm1 + score, lower_scores_matrix[i][j],
            )
            middle_backtrack_matrix[i][j] = "+"
            if middle_scores_matrix[i][j] == upper_scores_matrix[i][j]:
                middle_backtrack_matrix[i][j] = "U"
            elif middle_scores_matrix[i][j] == lower_scores_matrix[i][j]:
                middle_backtrack_matrix[i][j] = "L"

    score = middle_scores_matrix[lv][lw]

    # Backtrack to find the alignment
    i, j = lv, lw
    v_result, w_result = "", ""
    current_backtrack_matrix = middle_backtrack_matrix
    current_matrix_type = "M"

    while i > 0 or j > 0:
        direction = current_backtrack_matrix[i][j]
        if direction == "+":
            v_result = v[i-1] + v_result
            w_result = w[j-1] + w_result
            i -= 1
            j -= 1
        elif direction == "-":
            v_result = v[i-1] + v_result
            w_result = "-" + w_result
            i -= 1
        elif direction == "|":
            v_result = "-" + v_result
            w_result = w[j-1] + w_result
            j -= 1
        elif direction == "L":
            current_matrix_type = "L"
            current_backtrack_matrix = lower_backtrack_matrix
        elif direction == "U":
            current_matrix_type = "U"
            current_backtrack_matrix = upper_backtrack_matrix
        elif direction == "M":
            if current_matrix_type == "U":
                v_result = "-" + v_result
                w_result = w[j-1] + w_result
                j -= 1
            else:
                v_result = v[i-1] + v_result
                w_result = "-" + w_result
                i -= 1
            current_backtrack_matrix = middle_backtrack_matrix
            current_matrix_type = "M"

    return score, v_result, w_result

# Reading inputs and writing outputs
with open("input.txt") as infile:
    match_reward, mismatch_penalty, gap_open_penalty, gap_extend_penalty = map(int, infile.readline().strip().split())
    v = infile.readline().strip()
    w = infile.readline().strip()

score, aligned_v, aligned_w = AffineGapPenalties(v, w, match_reward, mismatch_penalty, gap_open_penalty, gap_extend_penalty)

with open("output.txt", "w") as outfile:
    outfile.write(f"{score}\n")
    outfile.write(f"{aligned_v}\n")
    outfile.write(f"{aligned_w}\n")
