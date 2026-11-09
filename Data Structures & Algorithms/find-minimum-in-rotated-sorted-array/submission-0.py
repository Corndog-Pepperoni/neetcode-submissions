class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # We will have found the minimum value when the left and right pointer meet
        while l < r:
            # Calculate the middle index
            m = l + ((r - l) // 2 )

            # If the current indexed value is less tahn the right pointer's value, move r to m
            if nums[m] < nums[r]:
                r = m
            # Otherwise if the current indexed value is more than or equal to the right pointer's value,
            # move l in front of m
            else:
                l = m + 1

        return nums[l]