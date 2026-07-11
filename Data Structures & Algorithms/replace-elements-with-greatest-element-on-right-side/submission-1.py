class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        rightMax = -1
        #brute force 
        for i in range(len(arr)-1, -1, -1):
            res[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return res

        