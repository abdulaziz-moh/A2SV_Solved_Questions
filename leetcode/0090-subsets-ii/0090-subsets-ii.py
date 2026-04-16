class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        self.n, ans = len(nums), [[]]
        def backtrack(idx, arr):
            if idx >= self.n:
                return
            for i in range(idx,self.n):
                arr.append(nums[i])
                cnt = Counter(arr)
                for v in ans:
                    if Counter(v) == cnt:
                        break
                else:
                    ans.append(arr[:])

                backtrack(i+1, arr)
                arr.pop()
        backtrack(0,[])
        return ans