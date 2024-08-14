class Solution:
    def longestCommonSubstr(self, S1, S2):
        n=len(S1)
        m=len(S2)
        dp=[[0]*(m+1) for i in range(n+1)]
        ma=0
        for i in range(n):
            for j in range(m):
                if S1[i]==S2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    ma=max(ma,dp[i+1][j+1])
                else:
                    dp[i+1][j+1]=0
        return ma