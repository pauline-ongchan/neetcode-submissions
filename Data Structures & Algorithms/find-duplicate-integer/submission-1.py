class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brute force
        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)
                
        