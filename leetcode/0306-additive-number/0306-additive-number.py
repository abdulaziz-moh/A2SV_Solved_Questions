class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        self.ans, self.n , arr = False, len(num), []

        def backtrack(idx):

            if idx >= self.n:
                 return len(arr) >= 3

            for i in range(idx+1, self.n + 1):

                if num[idx] == '0' and (i-idx) != 1:
                    break
                
                curr = int(num[idx:i])
                if len(arr) >= 2:
                    sm = arr[-1] + arr[-2]
                    if curr < sm:
                        continue
                    elif curr > sm:
                        break
                    
                arr.append(curr)
                if backtrack(i):
                    return True
                arr.pop()
            return False

        return backtrack(0)