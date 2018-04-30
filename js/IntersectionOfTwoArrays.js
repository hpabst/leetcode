

var intersection = function(nums1, nums2) {
    var ret = [];
    for(let i = 0; i < nums1.length; i++){
        if((nums2.includes(nums1[i])) && !(ret.includes(nums1[i]))){
            ret.push(nums1[i]);
        }
    }

    return ret;
};