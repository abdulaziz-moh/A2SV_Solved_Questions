class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            sqr = mid ** 2
            if sqr == x:
                return mid
            elif sqr > x:
                right =  mid - 1
            else:
                left = mid + 1
        return right


















        # left, right, mid = 0, x, 0

        # while right - left > 0.0000001:
        #     mid = left + (right - left) / 2
        #     if mid * mid == x:
        #         return int(mid)
        #     elif mid * mid < x:
        #         left = mid
        #     else:
        #         right = mid
        # print(mid)
        # return int(mid)

