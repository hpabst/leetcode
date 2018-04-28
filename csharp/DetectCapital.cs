using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class DetectCapital
    {
        public bool DetectCapitalUse(string word)
        {
            bool caseAllUpper = true;
            bool caseAllLower = true;
            bool caseTitle = true;
            for(int i = 0; i < word.Length; i++)
            {
                char c = word[i];
                caseAllUpper = caseAllUpper && Char.IsUpper(c);
                caseAllLower = caseAllLower && Char.IsLower(c);
                if (i == 0)
                {
                    caseTitle = caseTitle && Char.IsUpper(c);
                }
                else
                {
                    caseTitle = caseTitle && Char.IsLower(c);
                }
            }

            return caseAllUpper || caseAllLower || caseTitle;
        }
    }
}
