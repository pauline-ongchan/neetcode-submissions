class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        j=0
        while j < len(nums):
            prod = 1
            i=0
            temp = nums[j]
            nums[j] = 1
            while i < len(nums):
                prod *= nums[i]
                i += 1
            nums[j] = temp
            result[j] = prod
            j+=1
        return result
