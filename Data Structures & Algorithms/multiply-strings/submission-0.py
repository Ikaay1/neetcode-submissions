class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        power = 0
        int_num1 = int(num1)
        res = 0

        for i in range(len(num2)-1, -1, -1):
            num = int(num2[i])

            res += (num * int_num1) * (10 ** power)
            power += 1
        
        return str(res)

