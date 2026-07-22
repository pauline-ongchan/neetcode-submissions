class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        word = strs[0]
        print(word)
        prefix = ""
        flag = False
        if len(strs) == 1:
            return strs[0]
        for c in range(len(word)):
            letter = word[c]
            for i in range(1, len(strs)):
                if strs[i][c] == letter:
                    flag = True
                else:
                    flag = False
                    return prefix
            if flag:
                prefix += letter
        return prefix