class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        x = len(nums1) - 1
        # print(n)
        for i in range(m-1, -1, -1):
            nums1[x] = nums1[i]
            x -= 1
        
        i = 0
        left, right = n,0
        # print(nums1)
        while left < len(nums1) and right < n:
            if nums1[left] <= nums2[right]:
                nums1[i] = nums1[left]
                left += 1
            else:
                nums1[i] = nums2[right]
                right += 1
            i += 1
        while left < len(nums1):
            nums1[i] = nums1[left] 
            left += 1
            i += 1
        while right < n:
            nums1[i] = nums2[right]
            right += 1
            i += 1