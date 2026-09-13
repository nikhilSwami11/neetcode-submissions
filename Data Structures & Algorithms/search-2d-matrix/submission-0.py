class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def get_position(num: int):
            x = num // n
            y = num % n
            return (x,y)
        
        left = 0
        right = m*n - 1

        while left <= right:
            mid = left + (right - left)// 2
            x,y = get_position(mid)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                right = mid - 1
            else: left = mid + 1
        return False