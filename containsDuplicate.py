class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = set()
        for i in nums:
            if i not in num:
                num.add(i)
            else:
                return True
        return False
