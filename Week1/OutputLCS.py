import sys

def LCSBackTrack(v, w):
    backtrack = [["" for _ in range(len(w)+1)] for _ in range(len(v)+1)] 
    s = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max((s[i-1][j], s[i][j-1], s[i-1][j-1] + match))
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = "right"
            else:
                backtrack[i][j] = "down_right"
    return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "down":
        return OutputLCS(backtrack, v, i-1, j)
    if backtrack[i][j] == "right":
        return OutputLCS(backtrack, v, i, j-1)
    if backtrack[i][j] == "down_right":
        return OutputLCS(backtrack, v, i-1, j-1) + v[i - 1]

with open("input.txt") as infile:
    v = infile.readline().rstrip()
    w = infile.readline().rstrip()

backtrack = LCSBackTrack(v, w)
i = len(v)
j = len(w)
sys.setrecursionlimit(i*j)
print(OutputLCS(backtrack, v, i, j))