class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set left and right pointers
        l, r = 0, len(nums) - 1

        # While the left pointer is more than the right pointer
        while l <= r:
            # Calculate the middle of the list using the position of the left and right pointers
            m = l + ((r - l) // 2)

            # If the nums[middle] is more than the target, then move the right pointer right behind where
            # middle is
            if nums[m] > target:
                r = m - 1
            # If the nums[middle] is less than the target, then move the left pointer right in front of
            # where middle is
            elif nums[m] < target:
                l = m + 1
            # Otherwise, they both match, so return middle
            else:
                return m
        # Return -1 if target was not found
        return -1