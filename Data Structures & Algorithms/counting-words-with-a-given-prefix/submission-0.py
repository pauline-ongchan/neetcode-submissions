class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)
        count = 0
        for word in words:
            if word[0:pref_len] == pref:
                count += 1
        return count


        