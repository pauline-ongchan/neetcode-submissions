class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        ans = []
        for j in range(len(nums2)):
            if nums2[j] not in next_greatest:
                for x in range(j, len(nums2)):
                    if nums2[x] > nums2[j]:
                        next_greatest[nums2[j]] = nums2[x]
                        break
                    else:
                        next_greatest[nums2[j]] = -1

        for i in range(len(nums1)):
            ans.append(next_greatest[nums1[i]])
        return ans
            
