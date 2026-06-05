class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        res = 0
        cur_gas = 0
        need_at_least = 0

        for i in range(len(cost)):
            cur_gas += gas[i]
            if cur_gas < cost[i]:
                res = i+1
                need_at_least += abs(cost[i]-cur_gas)
                cur_gas = 0
            else:
                cur_gas -= cost[i]
                
        if need_at_least > cur_gas:
            return -1
        
        return res
