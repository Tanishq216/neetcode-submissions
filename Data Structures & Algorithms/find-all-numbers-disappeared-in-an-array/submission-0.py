class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        print(n)
        for i in range(1,n+1):
            if i not in nums:
                res.append(i)
            else:
                continue
        return res

        