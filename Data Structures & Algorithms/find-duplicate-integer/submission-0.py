class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brute force
        store = {}

        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
                return i
                
        