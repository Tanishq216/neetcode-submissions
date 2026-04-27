class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        counts = []
        nums = list(set(nums))
        nums.sort()
        print(nums)
        n = len(nums)
        for i in range(n):
            if nums[i]+1 in nums:
                count += 1
            elif nums[i] +1 not in nums:
                counts.append(count)
                count = 1
        return max(counts)
        
         
        
        