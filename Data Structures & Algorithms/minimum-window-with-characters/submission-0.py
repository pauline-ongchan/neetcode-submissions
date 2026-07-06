class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if empty, no mathc
        if t == "":
            return ""
        
        #initialize dicts
        countT, window = {}, {}

        #create the dict for t
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        #initialize have
        have = 0 
        #initialize distinct characters need to match
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                
                #shrink window from left side
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
            
        if resLen != float('infinity'):
            return s[l:r+1]
        else: 
            return ""

        
        #create a set for t 
        # t_set = set(t)
        # matched_set = set()
        # l = 0
        # min_substring = s
        # match = False

        # while l < len(s):
        #     if s[l] not in t_set:
        #         l += 1
        #     else: 
        #         matched_set = set()
        #         for r in range(l, len(s)):
        #             if s[r] in t_set:
        #                 matched_set.add(s[r])
        #                 if matched_set == t_set:
        #                     match = True
        #                     substring = s[l:r+1]
        #                     l += 1
        #                     if len(substring) <= len(min_substring):
        #                         min_subtring = substring
        #                     break
        #         l += 1            
                            
        # if match:
        #     return min_substring
        # else:
        #     return ""
                    

        #before the first occurence of anything in t, move left pointer
        #on the first occurence of anything in t, move right pointer
            # if s[r] is in set
            #   add to matched_set
            # if matched_set = set 
            #   substring = s[l:r+1]
            #   l += 1
            # if len(substring) < len(min_substring):
            #       min_substring = substring
        #return min_substring

        
       
        