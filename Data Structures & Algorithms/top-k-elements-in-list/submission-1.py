class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return None
        
        result = {}
        output = []
        for num in nums:
            if num not in result:
                result[num] = 1
            elif num in result:
                result[num] += 1
        print(result)
        for i in range(k):
            output.append(max(result, key = result.get))
            max_key = max(result,key = result.get)
            del result[max_key]
        print(output)
        return output
        

        
        