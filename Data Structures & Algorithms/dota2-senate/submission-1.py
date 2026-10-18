class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        total_rs = senate.count("R")
        total_ds = senate.count("D")

        if not total_rs:
            return "Dire"
        
        if not total_ds:
            return "Radiant"


        ds_removed = 0
        rs_removed = 0
        total_ds_removed = 0
        total_rs_removed = 0
        while senate:
            new_senate = []

            for party in senate:

                if party == "R":
                    if rs_removed:
                        rs_removed -= 1
                        continue
                    else:
                        ds_removed += 1
                        total_ds_removed += 1
                        new_senate.append("R")

                        if total_ds_removed == total_ds:
                            return "Radiant"
                else:
                    if ds_removed:
                        ds_removed -= 1
                        continue
                    else:
                        rs_removed += 1
                        total_rs_removed += 1
                        new_senate.append("D")
                
                        if total_rs_removed == total_rs:
                            return "Dire"
            
            print(new_senate)
            senate = new_senate

        return ""

