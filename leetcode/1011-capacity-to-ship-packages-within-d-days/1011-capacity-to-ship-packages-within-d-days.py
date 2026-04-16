class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

            def calc_days(w):
                sm, cnt = 0, 0
                for v in weights:
                    sm += v
                    if sm > w:
                        cnt += 1
                        sm = v
                if sm > 0:
                    cnt += 1
                return cnt

            left , right = max(weights), sum(weights)

            while left <= right:
                mid = (left + right) // 2

                if calc_days(mid) <= days:
                    right = mid - 1
                else:
                    left = mid + 1
            return right + 1