from functools import cache

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        [1,3,4,2,2,4]
        1,3 -> one side
        4 -> one side
        4 -> one side
        2,2, -> one side

        [1,5,6,3]

        if less than 4 sides -> return False
        we aren't guarenteed sortedness
        only integers

        [1,4,3,2,4,2]  -> [1,2,2,3,3,4,4]

        1 -> recurse()
        1 + 4 -> recurse()
        push(4)
        set = {i, i+2}
        1 + 3 -> recurse()

        
        def can_form_square():

            if len(sides) > 4:
                return False
            
            if len(sides) == 4:
                if len(set(sides)) == 1
                    return True
                return False

            side = 0
            for i in range(len(matchsticks)):
                if i in hashSet:
                    continue
                
                side += matchsticks[i]

                sides.append(side)
                hashSet.add(i)
                can_form_square()
                sides.pop()
                hashSet.remove(i)
        
        side = []
        hashSet = set()
        can_form_square()

        can_form_square(1, 0, 0, 0)
        can_form_square(1, 4, 0, 0)
        can_form_square(4, 4, 0, 0)
        can_form_square(4, 4, 2, 0)
        can_form_square(4, 4, 4, 0)
        can_form_square(4, 4, 4, 2)
        can_form_square(4, 4, 4, 4)

        can_form_square(i, side1, side2, side3, side4):

            if i == len(matchSticks):
                if side1 == side2 and side2 == side3:
                    return True
                return False


            return can_form_square(i+1, side1 + matchSticks[i], side2, side3, side4) or can_form_square(i+1, side1, side2 + matchSticks[i], side3, side4) or can_form_square(i+1, side1, side2, side3 + matchSticks[i], side4) or can_form_square(i+1, side1, side2, side3, side4 + matchSticks[i])
        
        return can_form_square(0, 0, 0, 0, 0)


        if len(sides) == 4:
            if len(set(sides)) == 1
                return True
            return False

        # -> [1,2,2,3,4,4]

        sides = []
        sides.append(matchSticks[i])
        recurse()
        sides.pop()
        
        sides = {}
        can_form_square(target)
            sides = {matchsticks[i]}
            i -> can_form_square(matchsticks[i])
            sides.remove(matchsticks[i])
            sides = {matchsticks[i] + matchsticks[i]+matchsticks[i+1]}
            i+(i+1) -> can_form_square()
            pop
            sides = {matchsticks[i] + matchsticks[i]+matchsticks[i+2]}
            i+(i+2) -> can_form_square()

        can_form_square()
            i+1 -> can_form_square(target)
        
        can_form_square()



        """

        """
        [1,3,4,2,2,4]

        can_form_square(0, 0, 0, 0, 0)
            can_form_square(1, 1, 0, 0, 0)
                can_form_square(1, 5, 0, 0, 0) -> False
                can_form_square(1, 1, 4, 0, 0)
                    can_form_square(1, 4, 4, 0, 0)
                        can_form_square(1, 4, 4, 2, 0)
                            can_form_square(1, 4, 4, 2, 4)
                                can_form_square(1, 4, 4, 4, 4) -> True
                can_form_square(1, 1, 0, 4, 0)
                can_form_square(1, 1, 0, 0, 4)
            can_form_square(1, 0, 1, 0, 0)
            can_form_square(1, 0, 0, 1, 0)
            can_form_square(1, 0, 0, 0, 1)
        """

        @cache
        def can_form_square(i, side1, side2, side3, side4):

            if i == len(matchsticks):
                if side1 == side2 and side2 == side3 and side3 == side4:
                    return True
                return False


            return can_form_square(i+1, side1 + matchsticks[i], side2, side3, side4) or can_form_square(i+1, side1, side2 + matchsticks[i], side3, side4) or can_form_square(i+1, side1, side2, side3 + matchsticks[i], side4) or can_form_square(i+1, side1, side2, side3, side4 + matchsticks[i])
        
        return can_form_square(0, 0, 0, 0, 0)