class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        size = len(nums)
        max_val = max(nums)
        c_list = [0]*(max_val + 1)
        for i in range (len(nums)):
            c_list[nums[i]] += 1
       
        max_key = max(c_list)
        return c_list.index(max_key)   

 
solution = Solution()

# Test Case 1
nums = [3, 3, 4, 2, 3, 3, 3]
print(solution.majorityElement(nums)) 