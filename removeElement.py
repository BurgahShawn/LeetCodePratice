class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i += 1
        print(nums)