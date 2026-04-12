class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        n, ans = len(s), []
        for i in range(n):
            hm, arr, cnt = {}, [], 0

            for j in range(i,n):
                arr.append(s[j])
                swap = s[j].swapcase()

                if swap in hm and not hm[swap]:
                    hm[swap] = True
                    cnt += 1
                elif s[j] not in hm and swap not in hm:
                    hm[s[j]] = False
                
                if len(hm) == cnt:
                    if len(arr) > len(ans):
                        ans = arr[:]

        return "".join(ans)