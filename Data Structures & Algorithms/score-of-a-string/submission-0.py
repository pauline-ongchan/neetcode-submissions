class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        prev = 0
        for c in s:
            ans += abs(ord(c) - prev)
            prev = ord(c)
        return ans - ord(s[0])
        