class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()  # Sort the greed factors in ascending order
        s.sort()  # Sort the cookie sizes in ascending order

        satisfied_children = 0
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                satisfied_children += 1
                i += 1
            j += 1

        return satisfied_children