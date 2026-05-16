class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index):

            if index == len(digits):
                if combination:
                    res.append("".join(combination))
                return

            for char in phone_map[digits[index]]:
                combination.append(char)
                dfs(index+1)
                combination.pop()

        res = [] 
        combination = [] 
        dfs(0)

        return res
