class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre = defaultdict(list)
        for cor, p in prerequisites:
            pre[p].append(cor)

        ans = []
        status = [0] * numCourses
        def find(node):
            if status[node] == 0:
                status[node] = 1
            elif status[node] == 1:
                return False

            for v in pre[node]:
                if status[v] == 2:
                    continue
                if not find(v):
                    return False
                    
            status[node] = 2
            # print(node)            
            ans.append(node)
            # print(ans)
            return True

        for i in range(numCourses):
            if status[i] == 0:
                temp = find(i)
                # print(temp)
                if not temp:
                    return []
        # print(ans)
        x = ans[::-1]
        return x
            