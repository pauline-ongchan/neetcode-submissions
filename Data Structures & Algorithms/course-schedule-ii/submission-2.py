class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for course, req in prerequisites:
            prereq[course].append(req)

        visiting = set()
        visited = set()
        result = []
        def dfs(course):
            if course in visiting:
                return False #cycle detected, return empty array
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return result