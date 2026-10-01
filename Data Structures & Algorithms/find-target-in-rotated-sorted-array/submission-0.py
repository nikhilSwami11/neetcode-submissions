class Solution:
    def search(self, nums: List[int], target: int) -> int:
        1,2,3,4,5,6

        n = len(nums)
        start = 0
        end = n-1

        while start <= end:
            mid = start + (end - start)//2

            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

