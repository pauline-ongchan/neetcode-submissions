class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if length of s1> length of s2 
        if len(s1) > len(s2):
            return False
        # False

        #initialize both arrays 
        s1Count = [0] * 26
        s2Count = [0] * 26

        #initialize left pointer 
        l = 0

        #building character frequency 
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        if s1Count == s2Count:
            return True

        #sliding window
        #len(s1) because we already built the freq of the first s2 len(s1)
        for r in range(len(s1), len(s2)): 
            # moving right pointer
            s2Count[ord(s2[r]) - ord('a')] += 1
            #moving left pointer 
            s2Count[ord(s2[l]) - ord('a')] -= 1

            if s1Count == s2Count:
                return True
            
            l += 1
        return False

            
            

        
        
        