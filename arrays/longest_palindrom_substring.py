class Solution:
  def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if (n < 1):
      return ""
    elif n == 1:
      return s
    s = list(s)
    max_len = 0
    pali = None
    matrix = [[None for x in range(n)] for x in range(n)]
    for x in range(n):
      matrix[x][x] = True
      max_len = 1
      pali = s[x]
    i = 0
    while (i + 1 < n):
      if s[i] == s[i + 1]:
        matrix[i][i + 1] = True
        max_len = 2
        pali = ''.join(s[i:i + 2])
      else:
        matrix[i][i + 1] = False
      i += 1
    for i in range(2, n):
      start = 0
      end = i
      while (end < n):
        if s[start] == s[end]:
          if matrix[start + 1][end - 1]:
            matrix[start][end] = True
            if (abs((end - start)) + 1) > max_len:
              max_len = abs(end - start)
              pali = ''.join(s[start:end + 1])
          else:
            matrix[start][end] = False
        else:
          matrix[start][end] = False
        start += 1
        end += 1
    return pali


if __name__ == "__main__":
  print(Solution().longestPalindrome("banana"))