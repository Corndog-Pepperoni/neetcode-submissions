class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapify returns a min heap
        # Make it a max heap by turning all the values of stones into negative values
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # Pop the two stones now and determine which ones to add based off the given
            # conditions
            # If both stones are the same weight, both are already destroyed, so there is
            # nothing to pop
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            # It doesn't matter whether x or y is more than the other
            # In both cases, you subtract the two stones
            # Therefore, check for both cases in one by simply checking if they their
            # difference is a truthy val
            if x - y:
                heapq.heappush(maxHeap, -(x - y))
        
        # Return the remaining weight, or 0 if all stones were destroyed
        return abs(maxHeap[0]) if maxHeap else 0