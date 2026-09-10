class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_arr = []
        for c in s:
            if c.isalnum():
                input_arr.append(c.lower())
        n = len(input_arr)
        left = 0
        right = n-1
        while left<=right:
            if input_arr[left] != input_arr[right]:
                return False
            left += 1
            right -=1

        return True
        
            