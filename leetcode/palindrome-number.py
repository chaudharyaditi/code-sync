class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # digit extraction (needs array)
        # if x < 0:
        #     return False
        # if x >= 0 and x <= 9:
        #     return True
        # dig = [int(d) for d in str(x)]
        # check = []
        # while x > 0:
        #     check.append(x%10)
        #     x = x//10
        # return dig == check

        # no array
        xcomp = x
        reverse = 0
        if x < 0:
             return False
        while x > 0:
            reverse = (reverse*10) + (x%10)
            x = x//10
        return xcomp == reverse