class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                chunk = s[i:j]

                if chunk == chunk[::-1] and len(chunk) > len(longest):
                    longest = chunk
        return longest