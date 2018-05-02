using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class ConstructBST
    {
        public TreeNode BuildTree(int[] preorder, int[] inorder)
        {
            return RecursiveBuildTree(new Queue<int>(preorder), new List<int>(inorder), 0, inorder.Length - 1);
        }

        private TreeNode RecursiveBuildTree(Queue<int> preorder, List<int> inorder, int startIndex, int endIndex)
        {
            if (startIndex == endIndex)
            {
                TreeNode ret = new TreeNode(preorder.Dequeue());
                return ret;
            } else if (startIndex > endIndex)
            {
                return null;
            }
            else
            {
                TreeNode ret = new TreeNode(preorder.Dequeue());
                int index = inorder.IndexOf(ret.val);
                ret.left = RecursiveBuildTree(preorder, inorder, startIndex, index - 1);
                ret.right = RecursiveBuildTree(preorder, inorder, index + 1, endIndex);
                return ret;
            }
        }
    }
}
