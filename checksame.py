from collections import defaultdict
class Solution:
    def isAnagram(self, s, t) :
        count_first = defaultdict(int)
        count_second = defaultdict(int)
        
        for i in s:
            count_first[i] += 1
        for i in t :
            count_second[i] += 1


        if len(count_first)!= len(count_second):
            return False

        for i in count_second:
            if count_second[i] != count_first[i]:
                return False
        return True
    

s = Solution()
print(s.isAnagram('ab','a'))
