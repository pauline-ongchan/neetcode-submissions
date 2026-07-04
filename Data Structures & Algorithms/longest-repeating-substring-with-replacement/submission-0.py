class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s)

        for c in charSet:
            #reset count and left pointer
            count = 0
            l = 0
            for r in range(len(s)):
                # keeping track of the freq of the curr c
                if s[r] == c:
                    count += 1
                
                # while the length of the substring - freq of curr c > k
                while (r - l + 1) - count > k:
                    # if it's the curr c, minus count
                    if s[l] == c:
                        count -= 1
                    # keep moving left pointer
                    l += 1
                
                res = max(res, r - l + 1)
        
        return res

        

        




        
        