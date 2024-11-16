class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = [] 

        for i in s:
            if i in '([{':
                k.append(i)
            else:
                if not k or (i == ')' and k[-1] != '(') or (i == '}' and k[-1] != '{') or (i == ']' and k[-1] != '['):
                    return False
                k.pop()
        return not k