# nums = [5, 6, 1, 2, 3]
# nums = [3, 4, 5, 6, 7, 1, 2]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize l, r
        l , r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m
        
        pivot = l 
        l, r = 0, len(nums) - 1

        # finding which subarray to search
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1





        