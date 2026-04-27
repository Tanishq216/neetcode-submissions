class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for number in numbers:
            remain = target - number
            if remain in numbers:
                return [numbers.index(number)+1,numbers.index(remain)+1]
        