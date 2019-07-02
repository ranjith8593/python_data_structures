class Solution:
  def findMedianSortedArrays(self, nums1, nums2) -> float:
    if len(nums1) > len(nums2):
      Solution().findMedianSortedArrays(nums2, nums1)
    low = 0
    high = len(nums1)
    x = len(nums1)
    endy = len(nums2)
    y = len(nums2)
    print("x", x)
    print("y", y)
    while (low <= high):
      partitionx = int((low + high) / 2)
      partitiony = int((x + y + 1) / 2 - partitionx)
      print("partitiony", partitiony)
      maxX = float('-inf') if partitionx == 0 else nums1[partitionx - 1]
      minX = float('inf') if partitionx == x else nums1[partitionx]
      maxY = float('-inf') if partitiony == 0 else nums2[partitiony - 1]
      minY = float('inf') if partitiony == y else nums2[partitiony]
      if maxX <= minY and maxY <= minX:
        if (x + y) % 2 == 0:
          return float((max(maxX, maxY) + min(minX, minY)) / 2)
        else:
          return float(max(maxX, maxY))
        break
      elif maxX > minY:
        high = partitionx - 1
      elif maxY > minX:
        low = partitionx + 1


if __name__ == "__main__":
  ip1 = [1, 3]
  ip2 = [2]
  print(Solution().findMedianSortedArrays(ip1, ip2))
