class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = []
        if 1 not in nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != 1:
                maxCount.append(count)
                count = 0

            else:
                count += 1
        maxCount.append(count)
        return max(maxCount)
            
        





        