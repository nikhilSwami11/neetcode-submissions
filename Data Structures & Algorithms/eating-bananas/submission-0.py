class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        

        while left <= right:
            speed = left + (right - left)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/speed)
            if hours <= h:
                right = speed - 1
            else:
                left = speed + 1
        return left
            
