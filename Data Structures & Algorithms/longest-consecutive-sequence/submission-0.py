class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make nums a set that will be used to see if the next num in the consecutive sequence
        # is present
        digits = set(nums)
        longest = 0

        for num in digits:
            # If a new sequence has started
            if num - 1 not in digits:
                # Start tracking the length of the consecutive sequence
                length = 1
                # Keep adding one to the length if the next num in the consecutive sequence is
                # in the set
                while num + length in digits:
                    length += 1

                # Reevaluate the longest consecutive sequence
                longest = max(longest, length)
        
        return longest