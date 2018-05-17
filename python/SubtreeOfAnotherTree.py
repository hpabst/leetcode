class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s, t):
        s_order = []
        t_order = []
        self.getPreorder(s, s_order)
        self.getPreorder(t, t_order)
        s_joined = ''.join(['#'+str(x)+'#' for x in s_order])
        t_joined = ''.join(['#'+str(x)+'#' for x in t_order])
        return t_joined in s_joined

    def getPreorder(self, root, current):
        current.append(root.val)
        if root.left is None:
            current.append('lnull')
        else:
            self.getPreorder(root.left, current)
        if root.right is None:
            current.append('rnull')
        else:
            self.getPreorder(root.right, current)
        return

s = Solution()
t_root = TreeNode(4)
t_root.left = TreeNode(1)
t_root.right = TreeNode(2)

s_root = TreeNode(3)
s_root.left = TreeNode(4)
s_root.left.left = TreeNode(1)
s_root.left.right = TreeNode(2)
s_root.right = TreeNode(5)

s.isSubtree(s_root, t_root)