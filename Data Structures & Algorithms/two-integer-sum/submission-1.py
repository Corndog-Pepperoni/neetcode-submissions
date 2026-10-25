class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap for faster search
        hash_nums = {}

        # Copy every value and index of nums into hash_nums
        # As it does that, check if target - value is in the dictionary already
        for i in range(len(nums)):
            if target - nums[i] in hash_nums:
                return [hash_nums[target - nums[i]], i]
            hash_nums[nums[i]] = i
        
        # If there's no twosum, then hash_nums will basically be a hashmap version of nums