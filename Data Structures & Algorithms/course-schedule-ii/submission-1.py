class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        
        def dfs(node):

            if node in visited:
                return ([], False)
            
            if node in explored:
                return ([], True)
            
            visited.add(node)
            explored.add(node)
            res = []

            for neighbor in graph[node]:
                nodes, is_possible = dfs(neighbor)

                if not is_possible:
                    return ([], False)

                for nei_node in nodes:
                    res.append(nei_node)
            
            visited.remove(node)
            res.append(node)

            return (res, True)
        
        explored = set()
        visited = set()
        result = []
        
        for node in range(numCourses):
            res, is_possible = dfs(node)
            if not is_possible:
                return []
            
            for nei_node in res:
                result.append(nei_node)
        
        return result