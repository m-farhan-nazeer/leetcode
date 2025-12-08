class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a*a + b*b
                c = int(math.sqrt(c2))  # fast integer sqrt
                if c*c == c2 and c <= n:
                    count += 1
        return count