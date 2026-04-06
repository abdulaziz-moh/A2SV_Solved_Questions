class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        x, n = len(houses), len(heaters)
        left, ans = 0, float('-inf')

        def binarysearch(left, target):
            l, r = left, x-1

            while l <= r:
                mid = (l + r) // 2
                if houses[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        for i in range(n-1):
            target = (heaters[i] + heaters[i+1]) / 2
            idx = binarysearch(left, target)
            if idx < left:
                continue
            if houses[idx] <= heaters[i]:
                ans = max(ans, heaters[i] - houses[left])
                left = idx + 1
            else:
                R = houses[idx] - heaters[i]
                L = abs(heaters[i] - houses[left])

                if R >= L:
                    ans = max(ans, R)
                    left = idx + 1
                else:
                    ans = max(ans, L)
                    target = heaters[i] + L
                    idx = binarysearch(left, target)
                    left = idx + 1
            if left >= x:
                break
        else:
            if len(heaters) >= 2:
                target = (heaters[-1] + heaters[-2]) / 2
                idx = binarysearch(left, target) + 1

                L = heaters[-1] - houses[idx]
                R = houses[-1] - heaters[-1]
                ans = max(ans, L, R)

            else:
                L = abs(heaters[0] - min(houses))
                R = abs(max(houses) - heaters[0])
                ans = max(ans, L, R)
        return ans