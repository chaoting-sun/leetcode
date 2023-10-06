### method: divide and conquer (TLE)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def recursion(prevX, prevY, finalX, finalY, cnt):
            if prevX == finalX and prevY == finalY:
                return cnt + 1
            
            Xcnt = Ycnt = 0

            if prevX < finalX:
                Xcnt = recursion(prevX+1, prevY, finalX, finalY, cnt)

            if prevY < finalY:
                Ycnt = recursion(prevX, prevY+1, finalX, finalY, cnt)

            return cnt + Xcnt + Ycnt

        return recursion(0, 0, n-1, m-1, 0)


### method2: dynamic programming

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n] * m
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        
