class Solution:
    def splitString(self, s: str) -> bool:
        
        ans = False
        def backtrack(string, path):
            nonlocal ans
            if not string:
                for i in range(len(path) - 1):
                    if int(path[i]) != int(path[i+1]) + 1:
                        break
                else:
                    if len(path) != 1:
                        ans = True
            
            for i in range(len(string)):
                path.append(string[:i+1])
                backtrack(string[i+1:], path)
                path.pop()
        backtrack(s, [])
        return ans