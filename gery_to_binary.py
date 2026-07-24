class Solution:    
    def grayToBinary(self, n):
        # code 
        # here
        num = int(self.find_binary(n))
        grey = self.binarytogrey(num)

    def find_binary(self,n):
        if n==0:
            return "0"
        if n==1:
            return "1"
        return self.find_binary(n//2) + str(n%2)

    def binarytogrey(self,num):
        if num == 1:
            return "1"
        if num == 0:
            return "0"
c = Solution()
print(c.grayToBinary(11))