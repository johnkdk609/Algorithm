class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d = [[] for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            d[i] = [0] * (i + 1)

        for i in range(rowIndex + 1):
            d[i][0] = 1
            d[i][-1] = 1

        if rowIndex >= 2:
            for i in range(2, rowIndex + 1):
                for j in range(1, i):
                    d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

        return d[-1]