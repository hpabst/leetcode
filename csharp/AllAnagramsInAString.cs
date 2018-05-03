using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class AllAnagramsInAString
    {
        public IList<int> FindAnagrams(string s, string p)
        {
            if (s.Equals("") || p.Equals("") || p.Length > s.Length)
            {
                return new List<int>();
            }
            List<int> indices = new List<int>();
            Dictionary<char, int> freqP = new Dictionary<char, int>(26);
            Dictionary<char, int> freqWin = new Dictionary<char, int>(26);
            foreach (char c in "abcdefghijklmnopqrstuvwxyz")
            {
                freqWin.Add(c, 0);
            }
            foreach (char c in p)
            {
                freqP[c] = freqP.ContainsKey(c) ? freqP[c] + 1 : 1;
            }
            for (int i = 0; i < p.Length; i++)
            {
                freqWin[s[i]] += 1;
            }
            for (int i = 0; i < s.Length - p.Length; i++)
            {
                if (freqP.Keys.All(k => freqP[k] == freqWin[k]))
                {
                    indices.Add(i);
                }
                freqWin[s[i]] -= 1;
                freqWin[s[i + p.Length]] += 1;
            }
            if (freqP.Keys.All(k => freqP[k] == freqWin[k]))
            {
                indices.Add(s.Length-p.Length);
            }
            return indices;
        }
    }
}
