def coin_combination(amount_val, denomination):
    # Note we add a zero value to warm up
    combination = [0] * (amount_val + 1)
    combination[0] = 1
    for coin in denomination:
        for amount in range(amount_val+1):
            if amount >= coin:
                combination[amount] += combination[amount - coin]
    return combination[amount_val]

def getCoinCombination(amount , deno):

    for i in deno:
        if amount > i:
            combo = 0
            for i in deno:
                combo += getCoinCombination(amount-i , deno)
            return combo
        if amount == 0:
            return 1
        if amount < 0:
            return 0





if __name__ == "__main__":
    comb = coin_combination(12, [1, 2, 5])
    print("combo", comb)
