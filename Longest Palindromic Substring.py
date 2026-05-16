class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            # Expand outward as long as we are within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            # (right - 1) - (left + 1) + 1 simplifies to right - left - 1
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindrome (e.g., "aba", center is 'b')
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindrome (e.g., "abba", center is between 'b' and 'b')
            len2 = expand_around_center(i, i + 1)

            # Get the maximum length found at this center
            max_len = max(len1, len2)

            # If we found a longer palindrome, update our start and end pointers
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring
        return s[start : end + 1]
