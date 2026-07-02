class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        calc = 0
        result = 0
        # creating the tallest left wall
        for i in range(len(height)):
            if i == 0:
                leftMax[i] = 0
            else: 
                leftMax[i] = max(height[:i]) 

        # creating the tallest right wall
        for i in range(len(height)):
            rightMax[i] = max(height[i:])

        # calculating area 
        for i in range(len(height)):
            calc = min(leftMax[i], rightMax[i]) - height[i]
            if calc > 0:
                result += calc
        return result
            

            
                

        
        