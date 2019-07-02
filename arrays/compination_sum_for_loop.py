from typing import List


class Solution:
    result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def DFS(array, target, path, res):
            if target < 0:
                return
            if target == 0:
                result.append(path)
            else:
                for i, x in enumerate(array):
                    if x <= target:
                        DFS(array[i:], target - x, path + [x], res)

        DFS(candidates, target, path, result)
        return result


if __name__ == "__main__":
    ip1 = [2, 3, 5]
    ip2 = [2, 3, 6, 7]
    result = Solution().combinationSum(ip1, 8)
    print(result)
    print(Solution().combinationSum(ip2, 7))
