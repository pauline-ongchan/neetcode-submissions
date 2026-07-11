class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        #brute force 
        for i in range(len(arr)-1):
            res[i] = max(arr[i+1:len(arr)])
        return res

        