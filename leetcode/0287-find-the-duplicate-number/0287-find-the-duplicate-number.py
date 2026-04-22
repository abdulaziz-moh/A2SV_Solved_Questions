class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while nums[i] - 1 != i:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]