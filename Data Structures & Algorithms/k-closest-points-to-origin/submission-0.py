class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []

        for x,y in points:
            heapq.heappush(min_heap,((- math.sqrt(x*x + y*y), x, y) ))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        ans = []
        for _, x,y in min_heap:
            ans.append([x,y])
        return ans