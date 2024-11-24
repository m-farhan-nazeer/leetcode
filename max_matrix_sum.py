class Solution:
    def maxMatrixSum(self, matrix) :
        res = 0
        minima = float("inf")
        count_neg = 0
        for row in matrix:
            for n in row :
                res += abs(n)
                minima = min(minima,abs(n))
                if n < 0:
                    count_neg += 1

        if count_neg % 2 != 0:
            res -= (2* minima)

        return res

        