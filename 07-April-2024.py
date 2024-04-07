class Solution:
	def maxDotProduct(self, n, m, a, b):
		dp = [[0 for i in range(n + 1)] 
             for j in range(m + 1)]
        for i in range(1, m + 1, 1):
            for j in range(i, n + 1, 1):
                dp[i][j] = max((dp[i - 1][j - 1] + (a[j - 1] * b[i - 1])) , dp[i][j - 1])

        return dp[m][n]