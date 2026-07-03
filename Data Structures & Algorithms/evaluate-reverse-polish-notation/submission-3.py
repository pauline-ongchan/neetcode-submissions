class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        arithmetic = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b,
            "*": lambda a, b : a * b,
            "/": lambda a, b : int(a / b),
        }
        for i in range(len(tokens)):
            if tokens[i] not in arithmetic:
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                answer = arithmetic[tokens[i]](second, first)
                stack.append(answer)
        return stack[-1]

        
        
        