class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        longest = 0

        window = set()

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[start])
                start += 1
            window.add(s[i])
            if len(window) > longest:
                longest = len(window)
        return longest

