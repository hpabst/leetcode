
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        return

class Solution:
    def buildTree(self, preorder, inorder):
        return self.recursive_build(preorder, inorder, 0, len(preorder)-1)

    def recursive_build(self, preorder, inorder, start_idx, end_idx):
        if start_idx == end_idx:
            ret = TreeNode(preorder.pop(0))
            ret.left = None
            ret.right = None
            return ret
        elif start_idx > end_idx:
            return None
        else:
            ret = TreeNode(preorder.pop(0))
            index = inorder.index(ret.val, start_idx, end_idx+1)
            ret.left = self.recursive_build(preorder, inorder, start_idx, index-1)
            ret.right = self.recursive_build(preorder, inorder, index+1, end_idx)
            return ret

s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])