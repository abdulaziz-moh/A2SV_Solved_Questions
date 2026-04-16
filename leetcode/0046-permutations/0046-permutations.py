class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        ans, visited = [], set()

        def backtrack(idx):

            if idx >= self.n:
                ans.append(nums[:])
                return

            for i in range(idx, self.n):
                nums[idx], nums[i] = nums[i], nums[idx]
                visited.add(nums[i])
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
                visited.discard(nums[i])
        backtrack(0)
        return ans