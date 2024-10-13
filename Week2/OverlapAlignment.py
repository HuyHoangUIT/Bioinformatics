with open('input.txt', 'r') as f:
    lines = f.readlines()
    Score = lines[0].split()
    Score = [int(i) for i in Score]

    v = lines[1].replace('\n', '')
    w = lines[2]


def PrepareMatrice(v, w):
    Diag = [[0] * (len(w)) for _ in range(len(v))]
    
    for i in range(len(v)):
        for j in range(len(w)):
            if v[i] == w[j]:
                Diag[i][j] = Score[0]
            else:
                Diag[i][j] = -Score[1]

    return Diag

def OverlapAlignment(v, w):
    Diag = PrepareMatrice(v, w)

    m = len(w)
    n = len(v)

    backtrack = [[0] * (m+1) for _ in range(n+1)] 

    S = [[] for _ in range(n+1)] 
    for i in range(0, n+1):
        S[i] = [0] * (m+1)


    for j in range(1, m+1):
        S[0][j] = S[0][j-1] - Score[2]
        backtrack[0][j] = 2
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            scores = [S[i-1][j-1] + Diag[i-1][j-1],
                      S[i][j-1] - Score[2], #right
                      S[i-1][j] - Score[2]] #down
            
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    i = n
    max_value = max(S[-1])

    align_v, align_w = '', ''

    import copy
    last_line = copy.deepcopy(S[-1])
    last_line.remove(0)
    j = last_line.index(max_value) + 1

    while i*j>0:
        if backtrack[i][j] == 2:  # down
            align_v = v[i-1] + align_v
            align_w = '-' + align_w
            i -= 1
        elif backtrack[i][j] == 1:  # right
            align_v = '-' + align_v
            align_w = w[j-1] + align_w
            j -= 1
        elif backtrack[i][j] == 0:  # diagonal
            align_v = v[i-1] + align_v
            align_w = w[j-1] + align_w
            i -= 1
            j -= 1

    return max_value, align_v, align_w

res, fir, sec = OverlapAlignment(v, w)

with open('output.txt', 'w') as f:
    f.write(str(res))
    f.write('\n')
    f.write(fir)
    f.write('\n')
    f.write(sec)