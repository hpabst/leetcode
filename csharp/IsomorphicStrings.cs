using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class IsomorphicStrings
    {
        public bool IsIsomorphic(string s, string t)
        {
            int orderS = 0, orderT = 0;
            Dictionary<char, int> dictS = new Dictionary<char, int>(), dictT = new Dictionary<char, int>();
            StringBuilder encodingS = new StringBuilder(), encodingT = new StringBuilder();
            for (int i = 0; i < s.Length; i++)
            {
                if (!dictS.ContainsKey(s[i]))
                {
                    dictS.Add(s[i], orderS);
                    orderS += 1;
                }
                encodingS.Append(dictS[s[i]].ToString());
                if (!dictT.ContainsKey(t[i]))
                {
                    dictT.Add(t[i], orderT);
                    orderT += 1;
                }
                encodingT.Append(dictT[t[i]].ToString());
            }
            return encodingS.ToString().Equals(encodingT.ToString());
        }
    }
}
