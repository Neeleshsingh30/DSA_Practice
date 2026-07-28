# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
#Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + #7.
#In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally #adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.


# create a class to solve the problem
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        # use dynamic programming to calculate the number of ways to tile the board
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1   
        dp[2] = 2
        dp[3] = 5

        # fill the dp array using the recurrence relation
        for i in range(4, n + 1):
            # dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp[i - 3]) % mod
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[n]
    
# example usage
solution = Solution()
n = 5
print(solution.numTilings(n))
