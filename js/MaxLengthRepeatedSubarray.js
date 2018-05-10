/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var findLength = function(A, B) {
    let current_max = 0;
    let prev_solutions = [];
    for(let i = 0; i < A.length+1; i++){
        prev_solutions[i] = [];
        for(let j = 0; j < B.length + 1; j++){
            prev_solutions[i][j] = 0;
            if(i > 0 && j > 0){
                if(A[i-1] === B[j-1]){
                    prev_solutions[i][j] = prev_solutions[i - 1][j - 1] + 1
                    if(prev_solutions[i][j] > current_max){
                        current_max = prev_solutions[i][j];
                    }
                }
            }
        }
    }
    return current_max;
};

let result = findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]);