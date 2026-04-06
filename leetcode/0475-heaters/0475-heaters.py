class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        print(houses)
        print(heaters)
        x, n = len(houses), len(heaters)
        left, ans = 0, float('-inf')

        def binarysearch(left, target):
            l, r = left, x-1

            while l <= r:
                mid = (l + r) // 2
                # print("mid: ", mid)
                if houses[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            print("right", r)
            return r

        
        for i in range(n-1):
            target = (heaters[i] + heaters[i+1]) / 2
            print("target: ", target)
            idx = binarysearch(left, target)
            # if idx <= 0:
            #     idx = 0
            if idx < left:
                continue
            # print(idx)
            if houses[idx] <= heaters[i]:
                ans = max(ans, heaters[i] - houses[left])
                left = idx + 1
                print("left : ", left)
            else:
                R = houses[idx] - heaters[i]
                L = abs(heaters[i] - houses[left])
                print(R," ",L)

                if R >= L:
                    ans = max(ans, R)
                    # print(R)
                    # print(ans)
                    left = idx + 1
                    print("left ", left)
                else:
                    ans = max(ans, L)
                    target = heaters[i] + L
                    idx = binarysearch(left, target)
                    left = idx + 1
                    print("left ", left)
            print("ans" , ans)
            print(left)
            if left >= x:
                break
        else:
            if len(heaters) >= 2:
                target = (heaters[-1] + heaters[-2]) / 2
                idx = binarysearch(left, target) + 1

                L = heaters[-1] - houses[idx]
                R = houses[-1] - heaters[-1]
                # print(L," ",R)
                ans = max(ans, L, R)

            else:
                L = abs(heaters[0] - min(houses))
                R = abs(max(houses) - heaters[0])
                ans = max(ans, L, R)
        # print("ans", ans)
        return ans
