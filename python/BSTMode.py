class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        vals = self.dfs(root)
        freqs = {}
        max_vals = []
        max_count = 0
        for v in vals:
            freqs[v] = freqs.get(v, 0) + 1
            if freqs[v] == max_count:
                max_vals.append(v)
            elif freqs[v] > max_count:
                max_vals = [v]
                max_count = freqs[v]
        return max_vals

    def dfs(self, root):
        if root is None:
            return []
        else:
            child_vals = [root.val]
            child_vals.extend(self.dfs(root.left))
            child_vals.extend(self.dfs(root.right))
            return child_vals


s = Solution()
node_root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(2)
node_root.right = child1
child1.right = child2
s.fineMode(node_root)