from typing import List
class Solution:
    result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def DFS(array, target, path, res ,  index):
            print(array)
            print("path",path)
            print("res", target)
            print(len(array))
            if index > len(array):
                return
            if target < 0:
                return
            if target == 0:
                result.append(path)
            if array[index] <= target:
                DFS(array, target - array[index], path + [array[index]], res, index)
                DFS(array, target - array[index], path + [array[index]], res , index + 1)

        DFS(candidates, target, path, result, 0)
        return result


if __name__ == "__main__":
    ip1 = [2, 3, 5]
    ip2 = [2,3,6,7]
    result = Solution().combinationSum(ip1, 8)
    print(result)
    print(Solution().combinationSum(ip2, 7))
