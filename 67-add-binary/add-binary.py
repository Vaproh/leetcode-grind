class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sol = int(a, 2) + int(b, 2)

        return str(bin(sol))[2:]