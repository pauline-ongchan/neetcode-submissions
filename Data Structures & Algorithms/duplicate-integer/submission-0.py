class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using sets but idk if u can 
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
        
        
        # # brute force:
        # for n in range (0, len(nums)):
        #     for j in range (n+1, len(nums)):
        #         if nums[n] == nums[j]:
        #             return True
        # return False

        