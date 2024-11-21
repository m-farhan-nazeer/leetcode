class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                
                return [my_dict[complement], i]
            my_dict[nums[i]] = i  
