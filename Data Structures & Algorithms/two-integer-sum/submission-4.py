class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff in digits:
                return [digits[diff], i]
            digits[x] = i
        