class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_to_index = {}
        answer =[]
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complement_to_index:
                answer = [complement_to_index[complement], i]
            else:
                complement_to_index[nums[i]] = i
        return answer
        