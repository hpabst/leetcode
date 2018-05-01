using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace LeetCode
{
    class BSTMode
    {
        public int[] FindMode(TreeNode root)
        {
            List<int> values = this.Dfs(root);
            Dictionary<int, int> frequencies = new Dictionary<int, int>();
            List<int> maxValues = new List<int>();
            int maxCount = 0;
            foreach (var v in values)
            {
                if (!frequencies.ContainsKey(v))
                {
                    frequencies.Add(v, 0);
                }
                frequencies[v] += 1;
                if (frequencies[v] == maxCount)
                {
                    maxValues.Add(v);
                } else if (frequencies[v] > maxCount)
                {
                    maxValues = new List<int>();
                    maxValues.Add(v);
                    maxCount = frequencies[v];
                }
            }
            return maxValues.ToArray();
        }

        private List<int> Dfs(TreeNode root)
        {
            if (root == null)
            {
                return new List<int>();
            }
            else
            {
                List<int> childValues = new List<int>();
                childValues.Add(root.val);
                childValues.AddRange(this.Dfs(root.left));
                childValues.AddRange(this.Dfs(root.right));
                return childValues;
            }
        }
    }
}
