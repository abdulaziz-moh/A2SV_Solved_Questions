class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        hm = {'a':['b','c'], 'b':['a','c'], 'c':['a','b']}
        self.count = 0
        self.ans, arr = "", []
        def backtrack(a):

            if len(arr) == n:
                self.count += 1
                if self.count == k:
                    self.ans = "".join(arr)
                return
            
            for v in a:
                arr.append(v)
                backtrack(hm[v])
                arr.pop()
        backtrack(['a','b','c'])
        return self.ans

