using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class FindDisappearedNumbers
    {
        public IList<int> FindDisappearedNumbersInArray(int[] nums)
        {
            HashSet<int> numSet = new HashSet<int>(nums);
            List<int> ret = new List<int>();
            for (int i = 1; i < nums.Length + 1; i++)
            {
                if (!numSet.Contains(i))
                {
                    ret.Add(i);
                }
            }
            return ret;
        }
    }
}
