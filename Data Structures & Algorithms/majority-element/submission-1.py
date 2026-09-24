class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        max_val = 0
        majority = nums[0]

        for n in nums:
            if n in dict:
                dict[n] = dict.get(n, 0) + 1
            else:
                dict[n] = 1
            
            if dict[n] > max_val:
                    majority = n
                    max_val = dict[n]
        
        return majority
        
        