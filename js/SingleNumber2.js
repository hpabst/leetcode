var singleNumber = function(nums) {
    let digit_set = new Set(nums);
    let digit_sum = 0;
    for(let n of digit_set){
        digit_sum += n;
    }
    let num_sum = nums.reduce(function(sum, val){ return sum + val;});
    return (digit_sum*3 - num_sum)/2;
};

singleNumber([2, 2, 3, 2]);