class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrows = len(grid)
        ncols = len(grid[0])
        sum = 0
        col_maxes = [0 for i in range(0, ncols)]
        row_maxes = [0 for i in range(0, nrows)]
        for i in range(0, nrows):
            row_maxes[i] = max(grid[i])
        for j in range(0, ncols):
            col_maxes[j] = max([r[j] for r in grid])
        for i in range(0,nrows):
            row_max = row_maxes[i]
            for j in range(0, ncols):
                result = min(row_max, col_maxes[j])
                sum += result - grid[i][j]
        return sum

