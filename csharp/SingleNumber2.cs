using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class SingleNumber2
    {
        public int SingleNumber(int[] nums)
        {
            checked
            {
                HashSet<int> digitSet = new HashSet<int>(nums);
                long digitSum = 0;
                foreach (var i in digitSet)
                {
                    digitSum += i;
                }
                long numsSum = 0;
                foreach (var i in nums)
                {
                    numsSum += i;
                }
                long result = (digitSum * 3 - numsSum) / 2;
                return (int)result;
            }
        }
    }
}
