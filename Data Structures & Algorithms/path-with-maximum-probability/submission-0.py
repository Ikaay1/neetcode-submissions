from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        
        graph = {0: [(1, 0.5), (2, 0.2)], 1: [(0, 0.5), (2, 0.5)], 2: [(1, 0.5), (0, 0.2)]}
        max_heap = [(1, start)]
        computed_path = {start: 1}

        while heap:

            cur_max_prob, node = heapq.heappop(max_heap)

            if node == end_node:
                return cur_max_prob

            for neighbor_node, probability in graph[node]:
                new_poss_probability = cur_max_prob * probability

                if neighbor_node not in computed_path or new_poss_probability > computed_path[neighbor_node]:
                    computed_path[neighbor_node] = new_poss_probability
                    heapq.heappush((new_poss_probability, neighbor_node))
        """

        graph = defaultdict(list)

        for i in range(len(edges)):
            node1, node2 = edges[i]
            graph[node1].append((node2, succProb[i]))
            graph[node2].append((node1, succProb[i]))
        
        max_heap = [(-1, start_node)]
        computed_path = {start_node: 1}

        while max_heap:

            neg_cur_max_prob, node = heapq.heappop(max_heap)
            cur_max_prob = -neg_cur_max_prob

            if node == end_node:
                return cur_max_prob

            for neighbor_node, probability in graph[node]:
                new_poss_probability = cur_max_prob * probability

                if neighbor_node not in computed_path or new_poss_probability > computed_path[neighbor_node]:
                    computed_path[neighbor_node] = new_poss_probability
                    heapq.heappush(max_heap, (-new_poss_probability, neighbor_node))
        
        return 0