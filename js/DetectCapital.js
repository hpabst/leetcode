

var detectCapitalUse = function(word){
    let case_all_upper = true;
    let case_all_lower = true;
    let case_title = true;
    for(let i = 0; i < word.length; i++){
        let c = word.charAt(i);
        case_all_upper = case_all_upper && (c === c.toUpperCase());
        case_all_lower = case_all_lower && (c !== c.toUpperCase());
        if(i === 0){
            case_title = case_title && (c === c.toUpperCase());
        } else {
            case_title = case_title && (c !== c.toUpperCase());
        }
    }
    return case_all_lower || case_all_upper || case_title;
};