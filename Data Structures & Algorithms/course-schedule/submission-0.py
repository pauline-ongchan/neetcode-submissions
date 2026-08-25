class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False # cycle detected
            if prereqs[crs] == []:
                return True #no prereqs

            visiting.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prereqs[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

        