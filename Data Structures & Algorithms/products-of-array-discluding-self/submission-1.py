class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            temp = nums[:]
            temp.pop(i)
            x = 1
            for i in range(len(temp)):
                x *= temp[i]
            result.append(x)
        return result


        