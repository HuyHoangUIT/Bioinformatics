def BWT(string):
    M = []
    arr = list(string)
    for i in range(len(string)):
        arr = arr[-1:] + arr[:-1]
        M.append(''.join(arr))
    M = sorted(M)
    last_col = ''.join(a[-1] for a in M)
    return last_col

with open("input.txt") as infile:
    string = infile.read().strip()

last_col = BWT(string)

with open("output.txt", "w") as outfile:
    outfile.write(last_col)