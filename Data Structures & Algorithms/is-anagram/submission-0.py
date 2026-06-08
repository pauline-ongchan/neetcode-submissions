class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        

        # #brute force
        # sorted_s = sorted(list(s))
        # sorted_t = sorted(list(t))
        # print (sorted_s, sorted_t)

        # if len(sorted_s) == len(sorted_t):
        #     for i in range (0, len(sorted_s)):
        #         if sorted_s[i] != sorted_t[i]:
        #             return False
        #     return True
        # else:
        #     return False

        