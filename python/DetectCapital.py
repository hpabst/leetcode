


class Solution:
    def detectCapitalUse(self, word):
        case_all_upper = True
        case_all_lower = True
        case_title = True
        for i in range(0, len(word)):
            c = word[i]
            case_all_upper = case_all_upper and c.isupper()
            case_all_lower = case_all_lower and not c.isupper()
            if i == 0:
                case_title = case_title and c.isupper()
            else:
                case_title = case_title and not c.isupper()
        return case_title or case_all_lower or case_all_upper
