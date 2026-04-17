class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def isvalid(dist):
            cnt = m - 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= dist:
                    cnt -= 1
                    prev = position[i]
            return cnt <= 0
        
        left, right = 0, 10**9
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            if isvalid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans