class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_arr, right_arr):
            left, right = 0,0
            ans = []
            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] <= right_arr[right]:
                    ans.append(left_arr[left])
                    left += 1
                else:
                    ans.append(right_arr[right])
                    right += 1
            ans.extend(left_arr[left:])
            ans.extend(right_arr[right:])
            return ans        

        def mergesort(left, right,arr):

            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_arr = mergesort(left, mid, arr)
            right_arr = mergesort(mid + 1, right, arr)

            return merge(left_arr, right_arr)

        return mergesort(0,len(nums)-1,nums)