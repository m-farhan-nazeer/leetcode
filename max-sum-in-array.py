from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums, k) :
        start = 0
        
        my_dict = defaultdict(int)
        cur_sum = 0 
        cur_max = 0
        for i in range (len(nums)):
            cur_sum += nums[i]
            my_dict[nums[i]] += 1


            if i - start+ 1 > k :
                cur_sum -= nums[start]
                my_dict[nums[start]] -= 1
                if my_dict[nums[start]] == 0:
                    my_dict.pop(nums[start])
                start += 1
            if len(my_dict)==k:
                cur_max = max(cur_sum,cur_max)
        return cur_max
    
nums = [2, 3, 4, 2, 1, 5, 1, 8]
k = 3
s = Solution()
print(s.maximumSubarraySum(nums, k)) 