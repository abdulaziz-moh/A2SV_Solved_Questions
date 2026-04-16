class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.n, wordset = len(s), set(wordDict)
        ans, arr = set(), []
        def backtrack(idx):
            if idx == self.n:
                ans.add(" ".join(arr))
                return
            
            for i in range(idx+1, self.n+1):
                string = s[idx:i]
                if string in wordset:
                    arr.append(string)
                    backtrack(i)
                    arr.pop()
                    
        backtrack(0)
        return list(ans)

