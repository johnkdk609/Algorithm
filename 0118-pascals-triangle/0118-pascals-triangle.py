class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        d = [[] for _ in range(numRows)]
        for i in range(numRows):
            d[i] = [0] * (i + 1)

        for i in range(numRows):
            d[i][0] = 1
            d[i][-1] = 1

        for i in range(2, numRows):
            for j in range(1, i):
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

        return d