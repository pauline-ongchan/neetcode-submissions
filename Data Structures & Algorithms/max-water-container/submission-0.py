class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        currprod =0
        start = 0
        end = len(heights) -1

        while start!=end:
            if heights[start] < heights[end]:
                currprod=min(heights[start], heights[end]) * (end-start)
                if currprod > answer:
                    answer = currprod
                start += 1
            else: 
                currprod=min(heights[start], heights[end]) * (end-start)
                if currprod > answer:
                    answer = currprod
                end -=1

        return answer