def count(coins, len_coins ,amount):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len_coins <= 0:
        return 0

    return count(coins, len_coins -1 , amount) + count(coins, len_coins, amount - coins[len_coins - 1])


if __name__ == "__main__":
    print(count([1, 2, 3], 3,4))
