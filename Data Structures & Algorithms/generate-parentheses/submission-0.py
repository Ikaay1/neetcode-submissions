class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(opening, closing):

            if opening > n or closing > opening:
                return
            
            if opening == n and closing == n:
                parentheses.append("".join(parenth))
                return

            parenth.append("(")
            backtrack(opening+1, closing)
            parenth.pop()

            parenth.append(")")
            backtrack(opening, closing+1)
            parenth.pop()
        
        parenth = []
        parentheses = []
        backtrack(0, 0)

        return parentheses