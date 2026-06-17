class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums)):
            a = nums[i]
            l = i + 1 
            r = len(nums) - 1
            
            if i > 0 and a == nums[i-1] :
                continue

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum == 0:
                    answer.append(list([a, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1
        return answer

# -4 -1 -1 0 1 2
#nums[i] + nums[j] == -nums[k]

