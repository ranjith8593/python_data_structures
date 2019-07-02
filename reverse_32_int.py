class Solution:
  def reverse(self, x: int) -> int:
    n_digits = len(str(abs(x)))
    new_digit = 0
    val = 1
    if x < 0:
      val = -1
    x = abs(x)
    while n_digits > 1:
      temp = x % 10
      new_digit = new_digit + temp * (10 ** (len(str(x)) - 1))
      x = int(x / 10)
      n_digits = len(str(x))
    final = val * (new_digit + x)
    if abs(final) > 2147483647:
      return 0
    else:
      return final

if __name__ == "__main__":
  print(Solution().reverse(1234))
  print(Solution().reverse(-1234))
  print(Solution().reverse(2147483647))