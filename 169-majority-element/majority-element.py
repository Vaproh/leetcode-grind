class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, numba = 0, 0

        for i in nums:
            if count == 0:
                numba = i
            
            if i == numba:
                count += 1
            else:
                count -= 1

        return numba