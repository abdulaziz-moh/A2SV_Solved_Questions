class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        heaters.append(float('inf'))
        i, ans = 0, float('-inf')
        for house in houses:
            while heaters[i] < house:
                i += 1
            min_dist = min( abs(house - heaters[i-1]), abs(heaters[i] - house) )
            ans = max(ans, min_dist)
        return ans