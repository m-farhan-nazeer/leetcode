from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums) :
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        for i in count:
            if count[i] > 1:
                return False
        return True
    
s = Solution()
print(s.hasDuplicate('abcda'))