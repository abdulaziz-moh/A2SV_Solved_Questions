class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n, ans = len(nums), set()
        for i in range(n):
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    ans.add(nums[i])
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return list(ans)