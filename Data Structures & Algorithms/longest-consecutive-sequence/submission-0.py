class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set()
        longest = 1

        for i in range(len(nums)):
            seen.add(nums[i])

        for i in range(len(nums)):
            if nums[i]-1 in seen:
                continue
            curr = nums[i]
            while curr in seen:
                curr += 1
            longest = max(longest, curr - nums[i])
        return longest
            