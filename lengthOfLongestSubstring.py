class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Start pointer of sliding window
        start = 0
        # End pointer of sliding window
        end = 0
        # Sliding window to store subsstrings
        window = set()
        # Track the maximum length of a given window
        max_length = 0
        # Loop through input string
        while end < len(s):
            if s[end] not in window:
                window.add(s[end])
                end += 1
                max_length = max(max_length, len(window))
            else:
                window.remove(s[start])
                start += 1
        return max_length