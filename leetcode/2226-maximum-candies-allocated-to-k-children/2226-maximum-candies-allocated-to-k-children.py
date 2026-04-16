class Solution(object):
    def maximumCandies(self, candies, k):
        def checkUp(mid):
            
            sum=0
            for i in range(len(candies)):
                sum+=candies[i]//mid
                if sum>=k:
                    return True
            return False

        left, right = 1, max(candies)
        while left <= right:  
            mid = (left + right) // 2
            if checkUp(mid):
                left = mid + 1
            else:
                right = mid - 1 
        return left-1