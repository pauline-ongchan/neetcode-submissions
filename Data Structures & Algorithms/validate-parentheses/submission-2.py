class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        pairing = {")" : "(", "]":"[", "}": "{"}
        
        for sym in s:
            if sym in pairing:
                if stack and pairing[sym] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        if len(stack) == 0:
            return True
        else:
            return False
        
            
        

        