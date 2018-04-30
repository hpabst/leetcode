
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let ret = [];
    let nums_set = new Set(nums);
    for(let i = 1; i < nums.length + 1; i++){
        if(!nums_set.has(i)){
            ret.push(i);
        }
    }
    return ret;
};