class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_count = 0
        left = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count

        # put it in a set 
        # if the next is in the set
        #   if prev count exists:
        #       if count > max_count
        #           max_count = count
        # 
        # empty set then store new var
        # return max_count



        