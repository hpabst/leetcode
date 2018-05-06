

class Solution:
    def singleNumber(self, nums):
        # Let X be the sum of the individual digits in our input, Y be the sum of our input, and x_j be our missing digit.
        # 3*X = Y + x_j + x_j
        # 3*X - Y = 2*x_j
        # (3*X - Y) / 2 = x_j
        missing_num = int((sum(set(nums)) * 3 - sum(nums))/2)
        return missing_num


s = Solution()
print(s.singleNumber([2, 2, 3, 2]))