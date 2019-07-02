def coin_combination(amount, deno):
    dp = [[0 for x in range(amount + 1)] for x in range(len(deno) + 1)]

    col = len(dp[0])
    row = len(dp)
    for i in range(1, row):
        for j in range(1, col):
            print(j)
            if j >= deno[i-1]:
                rem = j - deno[i-1]
                dp[i][j] = dp[i][j] + dp[rem][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)


if __name__ == "__main__":
    coin_combination(4, [1, 2, 3])
