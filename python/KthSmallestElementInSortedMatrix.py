class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        single_list = []
        for l in matrix:
            single_list += l
        single_list = sorted(single_list)
        return single_list[k-1]