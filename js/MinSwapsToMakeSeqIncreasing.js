/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var minSwap = function(A, B) {
    let swap_dp = [];
    let no_swap_dp = [];
    swap_dp[0] = 1;
    no_swap_dp[0] = 0;
    for(let i = 1; i < A.length; i++){
        swap_dp[i] = A.length;
        no_swap_dp[i] = A.length;
        if(A[i-1] < A[i] && B[i-1] < B[i]){
            no_swap_dp[i] = no_swap_dp[i-1];
            swap_dp[i] = swap_dp[i-1] + 1;
        }
        if(A[i-1] < B[i] && B[i-1] < A[i]){
            no_swap_dp[i] = Math.min(no_swap_dp[i], swap_dp[i-1]);
            swap_dp[i] = Math.min(swap_dp[i], no_swap_dp[i-1] + 1);
        }
    }
    return Math.min(swap_dp[A.length - 1], no_swap_dp[A.length - 1]);
};