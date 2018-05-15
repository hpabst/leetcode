using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class BinaryTreeLevelOrderTraversal
    {
        public IList<IList<int>> LevelOrder(TreeNode root)
        {
            if (root == null)
            {
                return new List<IList<int>>();
            }
            List<IList<int>> result = new List<IList<int>>();
            List<TreeNode> nodes = new List<TreeNode>();
            nodes.Add(root);
            while (nodes.Any())
            {
                List<int> currentLevel = new List<int>();
                List<TreeNode> nextLevel = new List<TreeNode>();
                foreach (var n in nodes)
                {
                    currentLevel.Add(n.val);
                    if (n.left != null)
                    {
                        nextLevel.Add(n.left);
                    }
                    if (n.right != null)
                    {
                        nextLevel.Add(n.right);
                    }
                }
                result.Add(currentLevel);
                nodes = nextLevel;
            }
            return result;
        }
    }
}
