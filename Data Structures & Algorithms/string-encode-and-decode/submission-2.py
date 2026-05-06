class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = []

        for string in strs:
            return_str.append(string + "\n")
        
        return "".join(return_str)

    def decode(self, s: str) -> List[str]:
        return_strs = s.split("\n")
        return_strs.pop()
        return return_strs
