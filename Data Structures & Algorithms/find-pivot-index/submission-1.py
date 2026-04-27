class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        #print(nums)
        for i in range(1,len(nums)-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i -1
            else:
                continue
        return -1
            
            
        