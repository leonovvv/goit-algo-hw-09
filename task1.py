def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = prev[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin

    return result


# Examples
amount = 113
print("Greedy algorithm result:", find_coins_greedy(amount))
print("Dynamic programming result:", find_min_coins(amount))
