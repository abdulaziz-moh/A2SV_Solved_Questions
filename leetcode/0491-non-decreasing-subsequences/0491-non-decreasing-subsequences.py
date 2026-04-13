class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.n = len(nums)
        ans, arr = [], []
        def backtrack(idx):
            if len(arr) >= 2 and arr not in ans:
                ans.append(arr[:])
            if idx >= self.n:
                return
            
            for i in range(idx, self.n):
                if not arr or nums[i] >= arr[-1]:
                    arr.append(nums[i])
                else:
                    continue
                backtrack(i+1)
                arr.pop()
        backtrack(0)
        return ans