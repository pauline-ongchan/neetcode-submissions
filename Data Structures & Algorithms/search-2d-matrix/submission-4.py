class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firsts = []
        row = 0
        for i in range(len(matrix)):
            firsts.append(matrix[i][0])
        print(firsts)
        i = 0
        while i < len(firsts):
            if target == firsts[i]:
                return True
            elif target > firsts[i]:
                i += 1
            else: 
                break
            row = i
        print(row)
        if row > 0:
            searchSpace = matrix[row - 1]
        else: 
            searchSpace = matrix[0]
        return self.binarySearch(searchSpace, target)

    def binarySearch(self, nums:List[int], target: int) -> bool:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return False


        