class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = {}
        
        for num in nums:
            if num in k:
                k[num] += 1
            else:
                k[num] = 1

        for key in k:
            if k[key] == 1:
                return key