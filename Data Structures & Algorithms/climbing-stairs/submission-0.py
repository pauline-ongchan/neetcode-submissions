class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        storage = [-1] * (n + 1)
        storage[0] = 0
        storage[1] = 1
        storage[2] = 2

        def dfs(i):
            if storage[i] != -1:
                return storage[i]
            
            storage[i] = dfs(i-1) + dfs(i-2)
            return storage[i]
        
        return dfs(n)
        