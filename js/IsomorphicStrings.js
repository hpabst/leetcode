/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let mapS = {};
    let mapT = {};
    let orderS = 0, orderT = 0;
    let encodingS = "", encodingT = "";
    for(let i = 0; i < s.length; i++){
        let charS = s.charAt(i);
        let charT = t.charAt(i);
        if(!(charS in mapS)){
            mapS[charS] = orderS;
            orderS += 1;
        }
        encodingS += mapS[charS];
        if(!(charT in mapT)){
            mapT[charT] = orderT;
            orderT += 1;
        }
        encodingT += mapT[charT];
    }
    return encodingS === encodingT;

};