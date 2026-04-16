class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.n = len(candidates)
        ans, arr = [], []
        def backtrack(idx):
            sm = sum(arr)
            if len(ans) > 150:
                return
            if sm == target:
                ans.append(arr[:])
                return 
            elif sm > target:
                return
            
            for i in range(idx,self.n):
                arr.append(candidates[i])
                backtrack(i)
                arr.pop()
        backtrack(0)
        return ans
                