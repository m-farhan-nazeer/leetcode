class Solution:
    def rotateTheBox(self, box):

        rows,cols = len(box),len(box[0])

        for i in range (rows):
            k = cols - 1
            for j in reversed(range(cols)):
                if box[i][j] == "#":
                    box[i][j] ,box[i][k] = box[i][k],box[i][j]
                    k = k - 1

                elif box[i][j] == "*" :
                    k = j-1



        result = []

        for i in range (cols):
            c = []
            for j in reversed(range(rows)):
                c.append(box[j][i])

            result.append(c)

        return result


s = Solution()
a = [["#",".","*","."],
    ["#","#","*","."]]
print(s.rotateTheBox(a))



        