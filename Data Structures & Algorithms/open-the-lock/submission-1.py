class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        """
        "0000" -> "9999" = 4 turns
        "9999" -> "8888" = 4 turns


        ["0000", 0]
        [("0000", 1)]
        """

        def get_neighbors(current_lock):
            # 0000 -> 1000, 9000, 0100, 0900
            neighbors = []

            for index in range(4):
                value_at_index = int(current_lock[index])
                first_new_value_at_index = (value_at_index + 1) % 10
                second_new_value_at_index = (value_at_index - 1) % 10

                first_string = current_lock[:index] + str(first_new_value_at_index) + current_lock[index+1:]
                second_string = current_lock[:index] + str(second_new_value_at_index) + current_lock[index+1:]

                if first_string not in set_deadends:
                    neighbors.append(first_string)
                
                if second_string not in set_deadends:
                    neighbors.append(second_string)
            
            return neighbors
        

        set_deadends = set(deadends)

        if "0000" in set_deadends:
            return -1
            
        queue = deque([("0000", 0)])
        processed = {"0000"}

        """
        deadends = ["1111","0120","2020","3333"], target = "5555"

        queue = [("0000", 0)]
        processed = {"0000"}
        # 0000 -> 1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009
        (9900, 2)
        (9990, 3)
        (9999, 4)
        (8999, 5)
        (8899, 6)
        (8889, 7)

        """
        while queue:

            current_lock, cur_distance = queue.popleft()

            if current_lock == target:
                return cur_distance

            for neighbor_lock in get_neighbors(current_lock):
                if neighbor_lock in processed:
                    continue
                
                processed.add(neighbor_lock)
                queue.append((neighbor_lock, cur_distance+1))
        
        return -1
            





