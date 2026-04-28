class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con,n_con = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                n_con += 1
            if nums[i] == 0:
                max_con = max(max_con, n_con)
                n_con = 0
        return max(max_con, n_con)
        