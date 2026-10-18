class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        senate = list(senate)
        count = index = 0

        while index < len(senate):
            party = senate[index]

            if party == "R":

                if count < 0:
                    senate.append("D")
                
                count += 1
            
            else:

                if count > 0:
                    senate.append("R")
                
                count -= 1
            
            index += 1
        
        return "Radiant" if count > 0 else "Dire"
        

