from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        start, end = min(position), max(position)
        elem = set(position)

        def isvalid(dist):
            cnt = m
            for i in range(start, end+1, dist):
                if i in elem:
                    cnt -= 1
            return cnt <= 0
        
        left, right = start, end
        ans = 0
        while left < right - 1:
            mid = (right + left) // 2
            print(mid - start)
            if isvalid(mid-start):
                ans = mid - left
                left = mid + 1
            else:
                right = mid - 1
        return ans

obj = Solution()
position = [5,4,3,2,1,1000000000]
m = 2
# position = [1,2,3,4,7] 
# m = 3

print("ans: ",obj.maxDistance(position, m))