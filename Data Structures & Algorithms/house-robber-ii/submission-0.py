class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def houseRobber(arr):
            cache = [-1] * len(arr)

            def dp(i):
                if i >= len(arr):
                    return 0

                if cache[i] != -1:
                    return cache[i]

                cache[i] = max(
                    arr[i] + dp(i + 2),
                    dp(i + 1)
                )
                return cache[i]

            return dp(0)

        return max(
            houseRobber(nums[:-1]),
            houseRobber(nums[1:])
        )