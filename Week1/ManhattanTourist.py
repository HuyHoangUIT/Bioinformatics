def ManhattanTourist(n, m, Down, Right):
    s = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
        
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + Right[0][j-1]
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + Down[i-1][j], s[i][j-1] + Right[i][j-1])
            
    return s[n][m]
    
with open("input.txt") as infile:
    n, m = map(int, infile.readline().rstrip().split())
    
    # Initialize Down and Right matrices properly
    Down = [list(map(int, infile.readline().rstrip().split())) for _ in range(n)]
    infile.readline()  # Skip the empty line
    Right = [list(map(int, infile.readline().rstrip().split())) for _ in range(n + 1)]

print(ManhattanTourist(n, m, Down, Right))