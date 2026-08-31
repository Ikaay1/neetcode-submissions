class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        
        graph = {0: [1], 1:[0, 3, 4], 2: [3], 3: [1, 2], 4: [1]}

        get_height(0, None)
            1+get_height(1, 0) -> 3
                1+get_height(3, 1) -> 2
                    1+get_heights(2, 3) -> 1
                1+get_height(4, 1)


        def get_height(node, parent):

            max_height = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                max_height = max(max_height, 1+get_height(neighbor, node))
            
            return max_height
        
        height_node = [(3, 0)]
        for node in range(n):
            height = get_height(node, None)
            height_node.append((height, node))
        
        height_node.sort()
        target_roots = [height_node[0][1]]
        min_height = height_node[0][0]

        for i in range(1, len(height_node)):
            height, node = height_node[i]
            if height > min_height:
                break
            
            target_roots.append(node)
        
        return target_roots
        """

        def get_graph():
            graph = defaultdict(list)

            for node1, node2 in edges:
                graph[node1].append(node2)
                graph[node2].append(node1)
            
            return graph

        graph = get_graph()

        def get_height(node, parent):

            max_height = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                max_height = max(max_height, 1+get_height(neighbor, node))
            
            return max_height
        
        height_node = []
        for node in range(n):
            height = get_height(node, None)
            height_node.append((height, node))
        
        height_node.sort()
        target_roots = [height_node[0][1]]
        min_height = height_node[0][0]

        for i in range(1, len(height_node)):
            height, node = height_node[i]
            if height > min_height:
                break
            
            target_roots.append(node)
        
        return target_roots