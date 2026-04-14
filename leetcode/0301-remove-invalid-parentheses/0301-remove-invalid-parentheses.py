class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(string):
            temp = []
            for v in string:
                if v == '(':
                    temp.append(v)
                elif v == ')':
                    if temp:
                        temp.pop()
                    else:
                        return False
            return temp == []

        level = {s}
        ans = []
        while level:
            for v in level:
                if isValid(v):
                    ans.append(v)
            if ans:
                break

            newlevel= set()
            for string in level:
                for i in range(len(v)):
                    newlevel.add(string[:i] + string[i+1:])
            level = newlevel
        if not ans:
            return [""]
        return ans