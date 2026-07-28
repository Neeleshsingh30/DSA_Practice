Question : You have a robot positioned on a grid with m rows and n columns. The robot starts at the top-left corner of the grid (position [0][0]) and wants to reach the bottom-right corner (position [m-1][n-1]).
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]
      
        dp[0][0] = 1
      
        for row in range(m):
            for col in range(n):
                if row > 0:
                    dp[row][col] += dp[row - 1][col]
                if col > 0:
                    dp[row][col] += dp[row][col - 1]
      
        # Return the number of unique paths to reach the bottom-right corner
        return dp[m - 1][n - 1]