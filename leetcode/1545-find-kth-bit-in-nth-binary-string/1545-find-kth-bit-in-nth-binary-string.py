class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        reverse = {'0':'1', '1':'0'}

        def findstr(n):
            if n == 1:
                return "0"

            temp = findstr(n-1)
            rev = []
            
            for i in range( len(temp)-1, -1, -1 ):
                rev.append(reverse[temp[i]])

            return temp + '1' + "".join(rev)

        s = findstr(n)
        return s[k-1]
