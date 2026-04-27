from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anogram_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            #print(key)
            anogram_dict[key].append(s)
            print(anogram_dict.values())
        return anogram_dict.values()
        


        

        
        