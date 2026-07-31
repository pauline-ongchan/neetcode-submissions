from _heapq import heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        x, y = 0, 0
        res = 0
        for i in stones:
            maxHeap.append(i * -1)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                res = x - y
                heapq.heappush(maxHeap, res)
            heapq.heapify(maxHeap)
        if maxHeap:
            return maxHeap[0] * -1
        return 0