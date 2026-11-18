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

            # If the weight of stone x is less than y
            if x < y:
                # The stone of weight y becomes y - x
                y = y - x
                
                # Add stone y into the heap because that is the stone that should be kept
                # Stone x was already destroyed
                heapq.heappush(maxHeap, -y)
            # If the weight of stone x is more than y
            elif x > y:
                # The stone of weight x becomes x - y
                x = x - y

                # Add stone x into the heap because that is the stone that should be kept
                # Stone y was already destroyed
                heapq.heappush(maxHeap, -x)
        
        # Return the remaining weight, or 0 if all stones were destroyed
        return abs(maxHeap[0]) if maxHeap else 0