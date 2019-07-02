class Solution:
  def maxArea(self, height) -> int:
    max_area = 0
    start = 0
    end = len(height) - 1
    while (start < end):
      length = min(height[start], height[end])
      area = length * (end - start)
      if area > max_area:
        max_area = area
      if height[start] > height[end]:
        end -= 1
      else:
        start += 1
    return max_area

if __name__ == "__main__":
  ip = [1,8,6,2,5,4,8,3,7]
  print(Solution().maxArea(ip))