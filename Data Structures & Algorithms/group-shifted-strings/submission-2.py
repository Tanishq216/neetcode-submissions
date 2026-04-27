class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                res[(-1)].append(string)
            else:
                char_diff = []
                i = 1
                while i < len(string):
                    char_diff.append(
                        (ord(string[i]) - ord(string[i-1])) % 26
                    )
                    i += 1
                res[tuple(char_diff)].append(string)
        print(res.items())
        return list(res.values())