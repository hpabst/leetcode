# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a
# function to search target in nums. If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.recursiveBS(nums, target, 0)

    def recursiveBS(self, nums, target, idx):
        if len(nums) == 1:
            if nums[0] == target:
                return idx
            else:
                return -1
        else:
            midpoint = int(len(nums)/2)
            if nums[midpoint] == target:
                return idx + midpoint
            elif target > nums[midpoint]:
                return self.recursiveBS(nums[midpoint:], target, idx + midpoint)
            else:
                return self.recursiveBS(nums[:midpoint], target, idx)


s = Solution()
print(s.search([-1,0,3,5,9,12], 12))
