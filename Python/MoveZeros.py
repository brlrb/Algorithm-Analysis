# Problem 283: Move Zeroes // LeetCode.com


class Solution:
    nums = [1,0,3,3,0,9,0,6]
    def moveZeroes(self, nums):

        """
        Do not return anything, modify nums in-place instead.
        """
        
        counter = 0
        counter2 = 0
        
        print(nums)
        for counter in range(len(nums)):
            if nums[counter] !=0:
                nums[counter2], nums[counter] = nums[counter], nums[counter2]
                counter2 = counter2 + 1
