import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        resulting_sum = 0
        min_K = r
        if len(piles) == h:
            return r
        else:
            while l < r:
                mid = (l + r) // 2
                divisor = mid
                resulting_sum = 0
                for i in piles:
                    resulting_sum += math.ceil(i / divisor)
                
                # identified if left or right 
                if resulting_sum > h:
                    l = mid + 1  
                else:
                    r = mid 
                    min_K = min(min_K, mid)
            return min_K


            
        