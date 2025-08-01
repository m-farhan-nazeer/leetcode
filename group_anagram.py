class Solution:
    
    def groupAnagrams(self, strs) :
        result = {}


        for i in strs:
            
            word = "".join(sorted(i))
            if word in result:
                result[word].append(i)
            else:
                result[word] = [i]
        print(result.values())
        group = list(result.values())

        return group
a = ["act","pots","tops","cat","stop","hat"]
s = Solution()
print(s.groupAnagrams(a))