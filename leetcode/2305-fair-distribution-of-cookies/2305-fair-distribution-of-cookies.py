class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        self.ans, bucket = inf, [0]*k
        def backtrack(idx, bucket):
            if idx >= len(cookies)-1:
                a = min(bucket)
                j = 0
                for i in range(len(bucket)):
                    if bucket[i] == a:
                        j = i
                bucket[j] += cookies[idx]
                self.ans = min(self.ans, max(bucket))
                bucket[j] -= cookies[idx]
                return
            if max(bucket) >self.ans:
                return
            
            for i in range(k):
                bucket[i] += cookies[idx]
                backtrack(idx + 1, bucket)
                bucket[i] -= cookies[idx]

        backtrack(0,bucket)
        return self.ans
            