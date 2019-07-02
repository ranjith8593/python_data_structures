def longest_common_substring(ip1, ip2):
    row = len(ip1)
    col = len(ip2)
    dp = [[0 for x in range(col + 1)] for x in range(row + 1)]
    ip_1 = list(ip1)
    ip_2 = list(ip2)
    max_len = 0
    max_str = None
    for iv, val1 in enumerate(ip_1):
        for jv, val2 in enumerate(ip_2):
            i = iv + 1
            j = jv + 1
            if val1 == val2:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_str = ''.join(ip_1[iv - max_len + 1:iv + 1])
    return max_len, max_str


if __name__ == "__main__":
    print(longest_common_substring("abcdxyz", "xyzabcd"))
