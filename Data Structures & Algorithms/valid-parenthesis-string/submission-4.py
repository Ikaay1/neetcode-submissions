class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lifeline = 0
        opening = []
        indices = {}

        for index, char in enumerate(s):
            if char == "*":
                lifeline += 1
            elif char == "(":
                opening.append(index)
            else:
                if not opening:
                    if not lifeline:
                        return False
                    else:
                        lifeline -= 1
                else:
                    opening.pop()
            
            indices[index] = lifeline

        for i in range(len(opening)-1, -1, -1):
            index = opening[i]
            after = lifeline - indices[index]

            if after <= 0:
                return False
            
            lifeline -= 1

        return True