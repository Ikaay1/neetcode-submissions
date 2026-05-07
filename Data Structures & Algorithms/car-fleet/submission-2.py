class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        queue = [0]*len(position)

        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            queue[i] = (position[i], time)
        
        queue.sort()
        fleets = 0

        while queue:
            pos, time = queue.pop()

            while queue and queue[-1][1] <= time:
                queue.pop()
            
            fleets += 1

        return fleets
