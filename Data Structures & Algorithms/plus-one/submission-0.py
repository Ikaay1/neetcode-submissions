class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        new_digits = []

        for digit in digits:
            new_digits.append(str(digit))
        
        digit_num = int("".join(new_digits)) + 1
        return [int(char) for char in str(digit_num)]
