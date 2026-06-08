class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_count = {}
        for num in nums:
            val_to_count[num] = 1 + val_to_count.get(num, 0)
        sorted_list = sorted(val_to_count.items(), key=lambda x:x[1], reverse=True)
        result = [key for key, value in sorted_list]
        return result[0:k]
        