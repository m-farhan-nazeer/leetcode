class Solution:
    def takeCharacters(self, s, k) :
        
        count = [0,0,0]

        for  i in s:
            count[ord(i) - ord("a")] += 1

        if min(count) < k:
            return -1
        


        res = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] -= 1

            while min(count) < k :
                count[ord(s[l])- ord("a")] += 1
                l += 1

            res = min(res,len(s) - (r-l+1))

        return res
    

s = Solution()
print(s.takeCharacters("aabaaaacaabc",2))
