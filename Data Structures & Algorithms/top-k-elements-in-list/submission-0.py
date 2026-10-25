class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = defaultdict(int)

        for num in nums:
            hash_nums[num] += 1
        
        # Return the sorted (in reverse order) keys of hash_nums by applying the key function
        # to every value of hash_nums

        # The key requires a function that is applied to every value in hash_nums
        
        # Sorted always returns a list (in this case, [hash_nums keys]), so we can take the
        # first k values through slicing
        return sorted(hash_nums, key=hash_nums.get, reverse=True)[:k]
