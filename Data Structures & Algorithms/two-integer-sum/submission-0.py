class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap for faster search
        hash_nums = {}

        # Copy every value and index of nums into hash_nums
        # As it does that, check if target - value is in the dictionary already
        for index, value in enumerate(nums):
            if target - value in hash_nums:
                return [hash_nums[target - value], index]
            hash_nums[value] = index
        
        # If there's no twosum, then hash_nums will basically be a hashmap version of nums