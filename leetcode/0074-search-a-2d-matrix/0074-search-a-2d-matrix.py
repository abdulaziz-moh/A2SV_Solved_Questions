class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def find(arr,target):
            left, right = 0,len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for arr in matrix:

            if target <= arr[-1] and find(arr,target):
                return True
            elif target < arr[0]:
                break

        return False