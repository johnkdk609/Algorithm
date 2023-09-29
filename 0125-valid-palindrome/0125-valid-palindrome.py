import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted_str = re.sub(r'\W+', '', s).lower()

        if len(extracted_str) == 0:
            return True

        left, right = 0, len(extracted_str) - 1

        while left < right:
            while not extracted_str[left].isalnum() and left < right:
                left += 1
            while not extracted_str[right].isalnum() and left < right:
                right -= 1

            if extracted_str[left] != extracted_str[right]:
                return False
            left += 1
            right -= 1

        return True