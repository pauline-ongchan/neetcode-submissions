class Solution:
    def isHappy(self, n: int) -> bool:
        # have a seen dictionary number -> true/false
        # divide n by 10 and 
        # square the remainder and add to result 
        # assign that to n 
        seen = set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = self.sumOfDigits(n)

        return True
    
    def sumOfDigits(self, n:int) -> int:
        temp = 0
        while n != 0:
            temp = temp + (n % 10) ** 2
            n = n // 10
        return temp