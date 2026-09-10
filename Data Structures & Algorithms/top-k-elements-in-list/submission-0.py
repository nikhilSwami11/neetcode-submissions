class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i],0) + 1
            
        min_heap = []
        for key,value in mp.items():
            heapq.heappush(min_heap, (value,key))
            if len(min_heap) > k:
               heapq.heappop(min_heap)
                
        res = []
        for value,key in min_heap:
            res.append(key)
        return res

        