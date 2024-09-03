class Solution:
    def minOperations(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if str1[i - 1] == str2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return m + n - 2 * dp[n]