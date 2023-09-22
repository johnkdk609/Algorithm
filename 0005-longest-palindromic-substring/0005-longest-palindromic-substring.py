class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Initialize a table to store palindrome information
        d = [[False] * n for _ in range(n)]

        start = 0   # Starting index of the longest palindrome substring
        max_length = 1  # Length of the longest palindrome substring

        # All substrings of length 1 are palindromes
        for i in range(n):
            d[i][i] = True

        # Check if the entire string is a palindrome
        if s == s[::-1]:
            return s

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                d[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length longer than 2
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1

                if d[i + 1][j - 1] and s[i] == s[j]:
                    d[i][j] = True

                    if k > max_length:
                        start = i
                        max_length = k

        # Extract the longest palindrome substring
        longest_palindrome = s[start:start + max_length]

        return longest_palindrome
