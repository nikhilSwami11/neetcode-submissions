class Solution:
    def climbStairs(self, n: int) -> int:
        n0, n1 = 1, 1

        for _ in range(n - 1):
            n0, n1 = n1, n0 + n1

        return n1