class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        swap_dp = [len(A) for i in range(0, len(A))]
        no_swap_dp = [len(A) for i in range(0, len(A))]
        swap_dp[0] = 1
        no_swap_dp[0] = 0
        for i in range(1, len(A)):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                no_swap_dp[i] = no_swap_dp[i-1]
                swap_dp[i] = swap_dp[i-1] + 1
            if A[i-1] < B[i] and B[i-1] < A[i]:
                no_swap_dp[i] = min(no_swap_dp[i], swap_dp[i-1])
                swap_dp[i] = min(swap_dp[i], no_swap_dp[i-1] + 1)
        return min(swap_dp[-1], no_swap_dp[-1])


s = Solution()
s.minSwap([1, 3, 5, 4], [1, 2, 3, 7])
