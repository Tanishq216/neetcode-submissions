class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            #print(str(strs))
            return str(strs)
        output = ""
        for string in strs:
            output= "<>".join(strs)
        return output

    def decode(self, s: str) -> List[str]:
        print(type(s))
        if s == "[]":
            s = []
            return []
        return s.split("<>")
