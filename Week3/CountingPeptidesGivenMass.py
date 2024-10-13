amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 
                     128, 129, 131, 137, 147, 156, 163, 186]

def count_peptides(mass):
    dp = [0] * (mass + 1)
    dp[0] = 1
    
    for i in range(1, mass + 1):
        for amino_mass in amino_acid_masses:
            if i >= amino_mass:
                dp[i] += dp[i - amino_mass]
    print(dp)
    return dp[mass]

mass = 57  
result = count_peptides(mass)
print(result)
