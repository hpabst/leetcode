/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    if(s === "" || p === "" || p.length > s.length){
        return [];
    }
    let indices = [];
    let freqP = {};
    let freqWin = {};
    let alpha = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < 26; i++){
        freqWin[alpha.charAt(i)] = 0;
    }
    for(let i = 0; i < p.length; i++){
        freqP[p.charAt(i)] = p.charAt(i) in freqP ? freqP[p.charAt(i)] + 1: 1;
    }
    for(let i = 0; i < p.length; i++){
        freqWin[s.charAt(i)] += 1;
    }
    for(let i = 0; i < s.length - p.length; i++){
        let all = true;
        for(let k in freqP){
            if(!(k in freqWin) || (freqP[k] !== freqWin[k])){
                all = false;
                break;
            }
        }
        if(all){
            indices.push(i);
        }
        freqWin[s[i]] -= 1;
        freqWin[s[i+p.length]] += 1;
    }
    let all = true;
    for(let k in freqP){
        if(!(k in freqWin) || (freqP[k] !== freqWin[k])){
            all = false;
            break;
        }
    }
    if(all){
        indices.push(s.length-p.length);
    }
    return indices;
};

findAnagrams("cbaebabacd", "abc");