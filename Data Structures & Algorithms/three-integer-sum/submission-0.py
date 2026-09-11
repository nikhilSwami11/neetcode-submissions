class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        ans = []
        for i in range(len(arr)-2):
            start = i + 1
            end = len(arr) - 1
            
            if i > 0 and arr[i] == arr[i - 1]:
                continue
                
            if arr[i] > 0:
                break

            while start < end:
                if arr[i] + arr[start] + arr[end] == 0:
                    ans.append([arr[i],arr[start],arr[end]])
                    start += 1
                    end -= 1
                    while start < end and arr[start] == arr[start - 1]:
                        start += 1
                    while start < end and arr[end] == arr[end + 1]:
                        end -= 1
                elif arr[i] + arr[start] + arr[end] < 0:
                    start +=1
                else:
                    end -=1
        return ans


