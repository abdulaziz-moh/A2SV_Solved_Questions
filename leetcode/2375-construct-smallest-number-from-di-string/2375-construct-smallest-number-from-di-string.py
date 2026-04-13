class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        nums = ['1','2','3','4','5','6','7','8','9']
        self.n, self.status = len(pattern), True
        ans, arr, visited = '', [], set()

        def backtrack():

            if len(arr) == self.n + 1:
                if self.status:
                    for i in range(self.n):
                        if (pattern[i] == 'I' and arr[i] > arr[i+1]) or (pattern[i] == 'D' and arr[i] < arr[i+1]) :
                            break
                    else:
                        self.ans = "".join(arr)
                        self.status = False
                return 

            for i in nums:
                if i not in visited:
                    arr.append(i)
                    visited.add(i)
                    backtrack()
                    arr.pop()
                    visited.discard(i)
        backtrack()
        return self.ans