class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        child_arr = self.getRow(rowIndex - 1)
        ans = [1]
        ans.extend(child_arr)
        for i in range(1, len(ans) - 1):
            ans[i] += ans[i+1]
        return ans