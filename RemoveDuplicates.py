class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        underCount = 0
        for i in range(1, len(nums)):
            if nums[i] == current:
                nums[i] = "_"
                underCount += 1
            else:
                current = nums[i]
        while underCount != 0:
            nums.remove("_")
            underCount -= 1

#%%
#not my solution, but it quite clean 
#The concept of iterating through a list using while is quite efficent
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)