def EditDistance(v, w):
    n = len(v)
    m = len(w)
    
    # Create a (n+1) x (m+1) matrix to store distances
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize the first column and first row of the matrix
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i - 1] == w[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No edit needed
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # Min of insert, delete, substitute
    
    return dp[n][m]

# Reading input from file
with open("input.txt") as infile:
    v = infile.readline().rstrip()
    w = infile.readline().rstrip()

# Output the result
print(EditDistance(v, w))
