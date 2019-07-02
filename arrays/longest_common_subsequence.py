def longest_common_subsequence(ip1, ip2):
    row = len(ip1)
    col = len(ip2)
    dp = [[0 for x in range(col+1)] for x in range(row+1)]
    ip_list_1 = list(ip1)
    ip_list_2 = list(ip2)
    for iv, temp1 in enumerate(ip_list_1):
        for jv, temp2 in enumerate(ip_list_2):
            i = iv + 1
            j = jv + 1
            if temp1 == temp2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[row][col]


if __name__ == "__main__":
    print(longest_common_subsequence("AGGTAB", "GXTXAYB"))
