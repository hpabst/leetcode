# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSumBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        triplet = sorted([nums[a], nums[b], nums[c]])
                        if triplet not in triplets:
                            triplets.append(triplet)
        return list(triplets)

    def threeSumNotarized(self, nums):
        sums = {}
        triplets = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                double = sorted([nums[a], nums[b]])
                double_sum = nums[a] + nums[b]
                if double_sum in sums.keys():
                    if double not in sums[double_sum]: sums[double_sum].append(double)
                else:
                    sums[double_sum] = [double]
        for c in set(nums):
            if -c in sums.keys():
                for double in sums[-c]:
                    triplets.append(double + [c])
        return triplets

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result


def testThreeSum():
    input_arr = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.threeSumNotarized(input_arr)
    print(result)


testThreeSum()