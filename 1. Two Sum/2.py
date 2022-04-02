class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in map:
                return [map[b], i]
            map[a] = i
        return []
