class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        # Given a string, left idx, and right idx
        # we can expand from those indexes to give us the largest length
        # or palindrome in that string
        def longestAtIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (r - l - 1, l + 1, r - 1)

        longest = 0
        start = 0
        end = 0
        
        # Iterate through the initial string array
        for i in range(len(s)):
            # For both odd and even centers
            for j in range(2):
                length, l, r = longestAtIndex(s, i, i + j)
                if length > longest:
                    longest = length
                    start = l
                    end = r
        
        # Resulting substring is the longest length substring
        return s[start:end + 1]