/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    let nrows = grid.length;
    let ncols = grid[0].length;
    let sum = 0;
    let col_maxes = [];
    let row_maxes = [];
    for(let i =0; i < nrows; i++){
        row_maxes.push(Math.max(...grid[i]));
    }
    for(let i = 0; i < ncols; i++){
        let colmax = 0;
        for(let j = 0; j < nrows; j++){
            colmax = Math.max(colmax, grid[j][i]);
        }
        col_maxes.push(colmax);
    }
    for(let i = 0; i < nrows; i++){
        let rowmax = row_maxes[i];
        for(let j = 0; j < ncols; j++){
            sum = sum + Math.min(rowmax, col_maxes[j]) - grid[i][j];
        }
    }
    return sum;
};

let grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]];
console.log(maxIncreaseKeepingSkyline(grid));