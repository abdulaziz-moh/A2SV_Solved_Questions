class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(len(gifts)):
            gifts[i] *= -1

        heapq.heapify(gifts)
        while abs(gifts[0]) > 0 and k > 0:
            item = -1 * (math.floor(math.sqrt(-1 * gifts[0])))
            heapq.heapreplace(gifts, item)
            k -= 1
        
        return (-1 * sum(gifts))