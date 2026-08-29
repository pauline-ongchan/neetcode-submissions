class Solution:
    def climbStairs(self, n: int) -> int:     
        prev, prev_prev = 1, 1

        for i in range(n - 1):
            temp = prev 
            prev = prev + prev_prev
            prev_prev = temp
        
        return prev