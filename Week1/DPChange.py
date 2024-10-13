def DPChange(money, Coins):
    MNCoins = [0]*(money+1) 
    for i in range(1, money + 1):
        min_coins = float('inf')
        for j in Coins:
            if i >= j:  
                num_coins = MNCoins[i - j] + 1
                if num_coins < min_coins:
                    min_coins = num_coins
        MNCoins[i] = min_coins
    return MNCoins[-1]
    
with open("input.txt") as infile:
    money = int(infile.readline().rstrip())
    Coins = [int(coin) for coin in infile.readline().rstrip().split()]

res = DPChange(money, Coins)
print(res)
