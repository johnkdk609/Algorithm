class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * 46
        d[1] = 1
        d[2] = 2

        for i in range(3, 46):
            if d[i] != 0:
                return d[i]
            else:
                d[i] = d[i - 1] + d[i - 2]
                
        return d[n]
