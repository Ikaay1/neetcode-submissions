class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        
        def dfs(node):

            if node in visited:
                return False
            
            if node in explored:
                return True
            
            visited.add(node)
            explored.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(node)

            return True
        
        explored = set()
        visited = set()
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True