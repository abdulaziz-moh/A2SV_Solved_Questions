class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        unq = set()
        for v in nums:
            if v in unq: 
                rep = v
            unq.add(v)

        for v in set([i for i in range(1, len(nums) + 1)]) - unq: 
            a = v
        return [rep, a]
