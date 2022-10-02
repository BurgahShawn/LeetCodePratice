class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numSet = set(range(1, len(nums)+1))


        for i in nums:
            if i in numSet:
                numSet.remove(i)
        return numSet