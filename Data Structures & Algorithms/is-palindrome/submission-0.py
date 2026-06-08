class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_arr =[]
        for c in s:
            if c.isalnum():
                word_arr.append(c.lower())
        for i in range(len(word_arr)):
            if word_arr[i] != word_arr[len(word_arr)-1-i]:
                return False
        return True


            
        