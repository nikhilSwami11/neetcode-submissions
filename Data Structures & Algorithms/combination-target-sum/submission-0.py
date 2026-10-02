class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        

        def backtrack(start_idx, curr_sum, arr):
            if curr_sum == target:
                res.append(arr[:])
                return
            
            for i in range(start_idx, len(nums)):
                num = nums[i]
                if curr_sum+num > target:
                    continue

                arr.append(num)
                backtrack(i, curr_sum + num, arr)
                arr.pop()
        
        backtrack(0,0,[])
        return res


