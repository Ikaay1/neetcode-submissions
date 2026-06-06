class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = 0
        maximum = max(hand)
        freq = [0]*(maximum+1)

        for num in hand:
            freq[num] += 1

        while count < len(hand):
            start_num = 0

            while not freq[start_num]:
                start_num += 1

            for num in range(start_num, start_num+groupSize):
                if num > maximum or not freq[num]:
                    return False
                
                freq[num] -= 1
                count += 1
        
        return True
