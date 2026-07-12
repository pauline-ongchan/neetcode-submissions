class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1 
        r = n 
        coins = 0
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) / 2
            if coins == n:
                return mid 
            elif coins > n:
                r = mid -1
            else:
                l = mid + 1
                res = max(res, mid) 
        return res

        