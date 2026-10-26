class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # chars stores char keys and index values
        # The index tells where a char was last seen
        chars = {}
        length = 0
        left = 0

        # enumerate yields index value pairs
        for index, char in enumerate(s):
            if char in chars:
                # chars[char] + 1 => take the index of where the char was last seen and move to the right
                # The current index of the left pointer may be more than chars[char] + 1, so take the max
                # because the left pointer shouldn't be going backwards
                left = max(left, chars[char] + 1)
            # Record the current char's index as a record of where it was last seen
            chars[char] = index
            # index - left + 1 => right pointer index minus the left pointer index
            # The +1 makes it so that the result is the number of chars in the window and not the number of
            # spaces between the left and right pointers
            length = max(length, index - left + 1)
        
        return length