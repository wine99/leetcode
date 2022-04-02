class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = []
        for i, x in enumerate(nums):
            sorted.append([x, i])
        sorted.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            sum = sorted[left][0] + sorted[right][0]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [sorted[left][1], sorted[right][1]]
        return []
