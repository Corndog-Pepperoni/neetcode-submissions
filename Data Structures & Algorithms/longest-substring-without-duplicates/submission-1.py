class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # chars keeps track of the characters in the substring so far
        # Also represents the window
        chars = set()
        length = 0
        left = 0

        # Set up the right pointer and move it
        for char in s:
            # If the right pointer's char is in chars, continue removing the left pointer's char from chars
            # and shifting it to the right until there are no longer any duplicates
            while char in chars:
                chars.remove(s[left])
                left += 1
            # Add the right pointer's char to chars, and compare the new length to the current one
            chars.add(char)
            length = max(length, len(chars))
        
        return length