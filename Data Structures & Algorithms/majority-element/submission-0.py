from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        frequent = count.most_common(1)
        return frequent[0][0]

         
        