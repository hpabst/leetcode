using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class MinSwapsToMakeSeqIncreasing
    {
        public int MinSwap(int[] A, int[] B)
        {
            int[] swapDp = new int[A.Length];
            int[] noSwapDp = new int[A.Length];
            swapDp[0] = 1;
            noSwapDp[0] = 0;
            for (int i = 1; i < A.Length; i++)
            {
                swapDp[i] = A.Length;
                noSwapDp[i] = A.Length;
                if (A[i - 1] < A[i] && B[i - 1] < B[i])
                {
                    noSwapDp[i] = noSwapDp[i - 1];
                    swapDp[i] = swapDp[i - 1] + 1;
                }
                if (A[i - 1] < B[i] && B[i - 1] < A[i])
                {
                    noSwapDp[i] = Math.Min(noSwapDp[i], swapDp[i - 1]);
                    swapDp[i] = Math.Min(swapDp[i], noSwapDp[i - 1] + 1);
                }
            }

            return Math.Min(swapDp[A.Length - 1], noSwapDp[A.Length - 1]);
        }
    }
}
