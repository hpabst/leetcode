using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class SubtreeOfAnotherTree
    {
        public bool IsSubtree(TreeNode s, TreeNode t)
        {
            List<string> sStrings = getPreorderStringList(s);
            List<string> tStrings = getPreorderStringList(t);
            StringBuilder sEncoding = new StringBuilder();
            StringBuilder tEncoding = new StringBuilder();
            foreach (string str in sStrings)
            {
                sEncoding.AppendFormat("#{0}#", str);
            }
            foreach (string str in tStrings)
            {
                tEncoding.AppendFormat("#{0}#", str);
            }
            return sEncoding.ToString().Contains(tEncoding.ToString());
        }

        public List<string> getPreorderStringList(TreeNode root)
        {
            List<string> left = new List<string>();
            List<string> right = new List<string>();
            if (root.left == null)
            {
                left.Add("lnull");
            }
            else
            {
                left = getPreorderStringList(root.left);
            }
            if (root.right == null)
            {
                right.Add("rnull");
            }
            else
            {
                right = getPreorderStringList(root.right);
            }
            List<string> ret = new List<string>();
            ret.Add(root.val.ToString());
            ret.AddRange(left);
            ret.AddRange(right);
            return ret;
        }
    }
}
