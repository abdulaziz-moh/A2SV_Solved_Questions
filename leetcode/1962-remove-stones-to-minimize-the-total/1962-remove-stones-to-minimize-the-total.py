class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] *= -1

        heapq.heapify(piles)
        while abs(piles[0]) > 0 and k > 0:
            item = piles[0] + ((piles[0] * (-1)) // 2)
            heapq.heapreplace(piles, item)
            k -= 1

        ans = 0
        for i in range(len(piles)):
            ans += piles[i] * (-1)
        return ans