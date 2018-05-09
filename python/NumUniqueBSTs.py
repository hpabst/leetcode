class Solution:
    def __init__(self):
        self.solutions = {}
        self.solutions[0] = 1
        self.solutions[1] = 1

    def numTrees(self, n):
        if n in self.solutions:
            return self.solutions[n]
        sum = 0
        for i in range(1, n+1):
            left_subtrees = self.numTrees(i-1)
            right_subtrees = self.numTrees(n-i)
            sum += left_subtrees * right_subtrees
        if n not in self.solutions:
            self.solutions[n] = sum
        return sum