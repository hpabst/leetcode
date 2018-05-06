using System.Collections.Generic;
using System.Linq;

namespace LeetCode
{
    class SymmetricTree
    {
        public bool IsSymmetric(TreeNode root)
        {
            if (root == null)
            {
                return true;
            }
            var currentLevel = new List<TreeNode>(new[]{root});
            var nextLevel = new List<TreeNode>();
            while (currentLevel.Any())
            {
                foreach (TreeNode t in currentLevel)
                {
                    nextLevel.Add(t.left);
                    nextLevel.Add(t.right);
                }
                for (var i = 0; i < currentLevel.Count; i++)
                {
                    if (nextLevel[i]?.val != nextLevel[nextLevel.Count - 1 - i]?.val)
                    {
                        return false;
                    }
                }
                nextLevel.RemoveAll(n => n == null);
                currentLevel = nextLevel;
                nextLevel = new List<TreeNode>();
            }
            return true;
        }
    }
}
