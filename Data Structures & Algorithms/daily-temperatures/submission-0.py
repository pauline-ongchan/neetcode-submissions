class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                ans_index = index.pop()
                result[ans_index] = i - ans_index
            else:
                stack.append(temperatures[i])
                index.append(i)
        return result
            
