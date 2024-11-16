class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z = str(x)
        l = list(z)
        y = l[::-1]
        
        while True:
            if l == y:
                return True
            else:
                return False
