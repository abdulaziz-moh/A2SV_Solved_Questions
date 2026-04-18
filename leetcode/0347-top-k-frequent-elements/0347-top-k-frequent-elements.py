class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        mn = min(count.values())
        rng = max(count.values()) - mn + 1
        bucket = [[] for _ in range(rng)]
        ans = []
        for v in count:
            bucket[count[v] - mn].append(v)

        for i in range(rng - 1, -1, -1):
            if len(bucket[i]) >= k:
                ans.extend(bucket[i][:k])
                k = 0
            else:
                ans.extend(bucket[i])
                k -= len(bucket[i])
                
        return ans