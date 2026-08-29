class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            # option of steal + skip next or skip
            cache[i] = max(
                nums[i] + dp(i+2),
                dp(i+1)
                )
            return cache[i]
        return dp(0)

        
        