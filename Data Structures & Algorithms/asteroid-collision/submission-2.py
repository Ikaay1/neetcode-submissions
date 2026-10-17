class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def is_diff_dir(asteroid1, asteroid2):

            if asteroid1 < 0 and asteroid2 < 0 or asteroid1 > 0 and asteroid2 > 0:
                return False
            
            return True
        
        stack = []

        for asteroid in asteroids:

            if asteroid > 0:
                stack.append(asteroid)
                continue

            while stack and stack[-1] > 0 and asteroid < 0 and abs(asteroid) > stack[-1]:
                stack.pop()
            
            """
            no stack
            stack and last is positive but bigger than or equal to abs(asteroid)
            stack and last is negative (same sign with asteroid)
            """
            if not stack or not is_diff_dir(stack[-1], asteroid):
                stack.append(asteroid)
            elif stack[-1] == abs(asteroid):
                stack.pop()
     
        return stack