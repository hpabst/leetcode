class Solution:
    def findLength(self, A, B):
        dp = [[0 for i in range(0, len(B) + 1)] for j in range(0, len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(max(i) for i in dp)

