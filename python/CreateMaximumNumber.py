




class Solution:
    max_maximal_size = 0
    def maxNumber(self, nums1, nums2, k):
        return [int(d) for d in str(self.maxNumberRecursive(nums1, nums2, k, 0))]

    def maxNumberRecursive(self, nums1, nums2, k, existing):
        if k == 0:
            return
        elif k == 1:
            max_digit = max(nums1+nums2)
            return existing*10 + max_digit
        sub_nums1 = nums1[:min(len(nums1), len(nums1) + len(nums2) - k + 1)]
        sub_nums2 = nums2[:min(len(nums2), len(nums1) + len(nums2) - k + 1)]
        max_digit = max(sub_nums1+sub_nums2)
        maximal1 = [(max_digit, i) for i, j in enumerate(sub_nums1) if j == max_digit]
        maximal2 = [(max_digit, i) for i, j in enumerate(sub_nums2) if j == max_digit]
        self.max_maximal_size = max(self.max_maximal_size, len(maximal1), len(maximal2))
        branches = []
        for n, i in maximal1:
            new = existing*10 + n
            result = self.maxNumberRecursive(nums1[i+1:], nums2, k-1, new)
            branches.append(result)
        for n, i in maximal2:
            new = existing*10 + n
            result = self.maxNumberRecursive(nums1, nums2[i+1:], k-1, new)
            branches.append(result)
        max_val = max(branches)
        return max_val


    def _collapse_digits(self, nums1):
        ret = 0
        for i in range(0, len(nums1)):
            ret *= 10
            ret += nums1[i]
        return ret
