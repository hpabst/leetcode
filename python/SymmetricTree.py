class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        current_level = [root]
        while len(current_level) > 0:
            next_level = []
            for n in current_level:
                next_level.append(n.left)
                next_level.append(n.right)
            for i in range(0, len(next_level)):
                if next_level[i] is None:
                    val1 = None
                else:
                    val1 = next_level[i].val
                if next_level[len(next_level)-1-i] is None:
                    val2 = None
                else:
                    val2 = next_level[len(next_level)-1-i].val
                if val1 != val2:
                    return False
            current_level = [n for n in next_level if n is not None]
        return True


root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.right.right = TreeNode(3)
root.right.left = TreeNode(4)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)
s = Solution()
s.isSymmetric(root)