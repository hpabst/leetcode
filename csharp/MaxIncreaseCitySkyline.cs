using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class MaxIncreaseCitySkyline
    {
        public int MaxIncreaseKeepingSkyline(int[][] grid)
        {
            int nRows = grid.Length;
            int nCols = grid[0].Length;
            int sum = 0;
            int[] colMaxes = new int[nCols];
            int[] rowMaxes = new int[nRows];
            for (int i = 0; i < nRows; i++)
            {
                rowMaxes[i] = grid[i].Max();
            }
            for (int i = 0; i < nCols; i++)
            {
                int colMax = 0;
                for (int j = 0; j < nRows; j++)
                {
                    colMax = Math.Max(colMax, grid[j][i]);
                }
                colMaxes[i] = colMax;
            }
            for (int i = 0; i < nRows; i++)
            {
                int rowMax = rowMaxes[i];
                for (int j = 0; j < nCols; j++)
                {
                    sum += Math.Min(rowMax, colMaxes[j]) - grid[i][j];
                }
            }
            return sum;
        }
    }
}
