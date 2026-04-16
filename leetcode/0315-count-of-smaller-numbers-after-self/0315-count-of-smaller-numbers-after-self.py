class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums = list(enumerate(nums))
        n =  len(nums)
        ans = [0] * n

        def merge(left_arr, right_arr):
            p1, p2 = 0,0
            n , m = len(left_arr), len(right_arr)
            retarr = []
            while p1 < n and p2 < m:
                if left_arr[p1][1] > right_arr[p2][1]:
                    retarr.append(left_arr[p1])
                    ans[left_arr[p1][0]] += (m - p2)
                    p1 += 1
                else:
                    retarr.append(right_arr[p2])
                    p2 += 1
            retarr.extend(left_arr[p1:])
            retarr.extend(right_arr[p2:])

            return retarr

        def mergesort(left, right):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2   

            left_arr = mergesort(left,mid)
            right_arr = mergesort(mid+1,right)

            return merge(left_arr, right_arr)

        mergesort(0, len(nums)-1)
        return ans 