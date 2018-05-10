using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class MaxLengthRepeatedSubarray
    {
        public int FindLength(int[] A, int[] B)
        {
            int[,] Dp = new int[A.Length + 1, B.Length + 1];
            for (int i = 1; i < A.Length + 1; i++)
            {
                for (int j = 1; j < B.Length + 1; j++)
                {
                    if (A[i - 1] == B[j - 1])
                    {
                        Dp[i, j] = Dp[i - 1, j - 1] + 1;
                    }
                }
            }
            return Dp.Cast<int>().Max();
        }
    }
}
