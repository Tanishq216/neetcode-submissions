class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                result.append(nums.index(nums[i]))
                result.append(nums.index(temp,nums.index(nums[i])+1))
                return result

        