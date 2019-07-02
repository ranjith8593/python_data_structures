class Solution:
  def isPalindrome(self, x: int) -> bool:
    a = ''.join(reversed(str(x)))
    x = str(x)
    return x == a

if __name__ == "__main__":
  print(Solution().isPalindrome(123))
