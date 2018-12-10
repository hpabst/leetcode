# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:

    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left - 1, right, ans, string + "(")
        if right:
            self.dfs(left, right - 1, ans, string + ")")

#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         if n == 0:
#             return []
#         elif n == 1:
#             return ["()"]
#         parentheses = []
#         tree_root = Node("", n-1, n-1)
#         tree_root.create_children()
#
#         def dfs(root):
#             if root.left is None and root.right is None:
#                 parentheses.append(root.parentheses_pattern)
#                 return
#             if root.left is not None:
#                 dfs(root.left)
#             if root.right is not None:
#                 dfs(root.right)
#             return
#
#         dfs(tree_root)
#         updated_parens = []
#         if n > 2:
#             parentheses = parentheses[1:]
#         for p in parentheses:
#             updated_parens.append("(" + p + ")")
#         return updated_parens
#
#
# class Node:
#     left = None
#     right = None
#     parentheses_pattern = ""
#     left_facing = 0
#     right_facing = 0
#
#     def __init__(self, pattern, left_parens, right_parens):
#         self.parentheses_pattern = pattern
#         self.left_facing = left_parens
#         self.right_facing = right_parens
#         return
#
#     def create_children(self):
#         if self.left_facing == 0 and self.right_facing == 0:
#             return
#         if self.left_facing > 0:
#             left_child = Node(self.parentheses_pattern+")", self.left_facing-1, self.right_facing)
#             left_child.create_children()
#             self.left = left_child
#         if self.right_facing > 0:
#             right_child = Node(self.parentheses_pattern+"(", self.left_facing, self.right_facing-1)
#             right_child.create_children()
#             self.right = right_child
#         return

s = Solution()
print(s.generateParenthesis(3))
