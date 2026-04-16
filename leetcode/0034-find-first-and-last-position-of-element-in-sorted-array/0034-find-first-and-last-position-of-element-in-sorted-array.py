class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bisect_left(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right + 1
        a = bisect_left(target)
        b = bisect_left(target + 1)
        if b-a == 0:
            return [-1,-1]
        else:
            return [a, b-1]
