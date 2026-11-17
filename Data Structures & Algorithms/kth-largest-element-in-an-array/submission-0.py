import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Iterate through the array
        # Add to min heap
        # If the current element added is smaller than the root, swap their spots
        # Then check if the length of the min heap array is greater than k
        # In that case, pop the root and select the smaller of the children elements to be the new root
        # Repeat until done iterating through the original array
        # Return the root
        min_heap = []
        heapq.heapify(min_heap)

        for i in range(0, len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                    heapq.heappop(min_heap)
        
        return min_heap[0]