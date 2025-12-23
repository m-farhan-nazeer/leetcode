class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m   # dp[j] = longest valid sequence ending at j

        for j in range(m):
            for k in range(j):
                valid = True
                for i in range(n):
                    if strs[i][k] > strs[i][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[k] + 1)

        return m - max(dp)
