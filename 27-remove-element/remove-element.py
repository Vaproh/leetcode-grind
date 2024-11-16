class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                k += 1
            else:
                i += 1