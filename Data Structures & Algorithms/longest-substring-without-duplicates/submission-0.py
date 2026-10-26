class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # chars keeps track of the characters in the substring so far
        chars = set()
        length = 0
        left = 0

        # Set up the right pointer and move it
        for right in range(len(s)):
            # If the right pointer's char is in chars, continue removing the left pointer's char from chars
            # and shifting it to the right until there are no longer any duplicates
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            # Add the right pointer's char to chars, and compare the new length to the current one
            chars.add(s[right])
            # right - left + 1 because were counting the amount of spaces between r and l
            # To get the amount of letters in the window, add 1
            length = max(length, right - left + 1)
        
        return length