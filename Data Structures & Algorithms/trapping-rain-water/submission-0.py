class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left =  [0]*n
        right = [0]*n

        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])
            right[n- i - 1] = max(right[n-i], height[n-i])
        water = 0
        for i in range(n):
            water += max(0, min(left[i],right[i])- height[i])
        return water