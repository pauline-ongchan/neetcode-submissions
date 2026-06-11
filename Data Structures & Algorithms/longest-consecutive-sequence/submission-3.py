class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_length = 0
        max_length = 0
        num_set = set(nums)
        if not nums:
            return 0
        for num in num_set:
            if (num-1) not in num_set:
                current_num = num
                curr_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    curr_length += 1
            max_length = max(max_length, curr_length)
        return max_length

            




        # nums_sorted = sorted(set(nums))
        # max_length = 1
        # curr_length = 1
        # if not nums:
        #     return 0
        # for i in range(len(nums_sorted)-1):
        #     if nums_sorted[i] + 1 == nums_sorted[i+1]:
        #         curr_length += 1
        #     else:
        #         curr_length = 1
        #     max_length = max(max_length, curr_length)
        # return max_length

        # 2, 20, 4, 10, 3, 4, 5
        # 2, 3, 4, 4, 5, 10, 20
        # 0, 2, 3, 4, 5, 6, 7