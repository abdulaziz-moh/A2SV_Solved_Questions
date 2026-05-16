class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        while k > 0:
            ans = heappop(nums)
            k -= 1
        return ans * (-1)