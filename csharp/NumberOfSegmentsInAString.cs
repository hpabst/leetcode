using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class NumberOfSegmentsInAString
    {
        public int CountSegments(string s)
        {
            int numSegments = 0;
            for (int i = 0; i < s.Length; i++)
            {
                if ((i == 0 || s[i - 1] == ' ') && s[i] != ' ')
                {
                    numSegments += 1;
                }
            }
            return numSegments;
        }
    }
}
