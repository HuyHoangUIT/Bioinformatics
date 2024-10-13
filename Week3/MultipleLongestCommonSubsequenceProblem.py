def multiple_lcs(X, Y, Z):
    len_x, len_y, len_z = len(X), len(Y), len(Z)
    
    # Initialize the DP table
    dp = [[[0] * (len_z + 1) for _ in range(len_y + 1)] for _ in range(len_x + 1)]
    
    # Fill the DP table
    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            for k in range(1, len_z + 1):
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    # Length of the longest common subsequence
    lcs_length = dp[len_x][len_y][len_z]
    
    # Backtracking to find the alignment
    def backtrack(i, j, k):
        if i == 0 or j == 0 or k == 0:
            return [], [], []
        
        if X[i - 1] == Y[j - 1] == Z[k - 1]:
            align_x, align_y, align_z = backtrack(i - 1, j - 1, k - 1)
            return align_x + [X[i - 1]], align_y + [Y[j - 1]], align_z + [Z[k - 1]]
        
        if dp[i - 1][j][k] >= max(dp[i][j - 1][k], dp[i][j][k - 1]):
            align_x, align_y, align_z = backtrack(i - 1, j, k)
            return align_x + [X[i - 1]], align_y + ['-'], align_z + ['-']
        
        if dp[i][j - 1][k] >= dp[i][j][k - 1]:
            align_x, align_y, align_z = backtrack(i, j - 1, k)
            return align_x + ['-'], align_y + [Y[j - 1]], align_z + ['-']
        
        align_x, align_y, align_z = backtrack(i, j, k - 1)
        return align_x + ['-'], align_y + ['-'], align_z + [Z[k - 1]]
    
    align_x, align_y, align_z = backtrack(len_x, len_y, len_z)
    
    # Format the output
    aligned_x = ''.join(align_x)
    aligned_y = ''.join(align_y)
    aligned_z = ''.join(align_z)
    
    return lcs_length, aligned_x, aligned_y, aligned_z

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # Read input from file
    with open(input_file, 'r') as file:
        X = file.readline().strip()
        Y = file.readline().strip()
        Z = file.readline().strip()
    
    # Compute the LCS and alignment
    lcs_length, aligned_x, aligned_y, aligned_z = multiple_lcs(X, Y, Z)
    
    # Write the output to file
    with open(output_file, 'w') as file:
        file.write(f"{lcs_length}\n")
        file.write(f"{aligned_x}\n")
        file.write(f"{aligned_y}\n")
        file.write(f"{aligned_z}\n")

if __name__ == "__main__":
    main()
