class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        left, right = 0, len(str(x)) - 1

        j = str(x)

        for num in range(len(j)):
            if j[left] == j[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
