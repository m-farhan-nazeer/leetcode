class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        my_dict = {}
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in my_dict and my_dict[s[i]] >= start:
                start = my_dict[s[i]] + 1
            
            my_dict[s[i]] = i
            
            length = i - start + 1
            max_len = max(max_len, length)

        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  
print(solution.lengthOfLongestSubstring("bbbbb"))    
print(solution.lengthOfLongestSubstring("pwwkew"))   
