class Solution:
    def pascalTriangleI(self, r, c):
        n = r - 1
        k = c - 1
        ans = 1

        for i in range(1, k + 1):
            ans = ans * (n - i + 1) // i

        return ans
