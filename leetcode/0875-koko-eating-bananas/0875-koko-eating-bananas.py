class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hour_it_takes(num_bananas):
            sm = 0
            for v in piles:
                sm += math.ceil(v/num_bananas)
            return sm <= h

        left, right = 1, sum(piles)

        while left <= right:
            mid = (left + right) // 2

            if hour_it_takes(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right + 1
                