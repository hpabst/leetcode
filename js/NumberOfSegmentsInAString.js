/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    let numSegments = 0;
    for(let i = 0; i < s.length; i++){
        if((i === 0 || s.charAt(i-1) === ' ') && s.charAt(i) !== ' '){
            numSegments += 1;
        }
    }
    return numSegments;
};