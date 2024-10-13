def MinNumCoins(m):
    Coins = [1, 4, 5]
    MNCoins = [0]*(m+1) 
    for i in range(1, m + 1):
        min_coins = float('inf')
        for j in Coins:
            if i >= j:  
                num_coins = MNCoins[i - j] + 1
                if num_coins < min_coins:
                    min_coins = num_coins
        MNCoins[i] = min_coins
    return MNCoins

res = MinNumCoins(22)
for i in range(len(res)):
    print(res[i], end = " ")
