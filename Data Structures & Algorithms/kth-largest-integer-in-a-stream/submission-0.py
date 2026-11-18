class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapifying returns None; it rearranges nums in place
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        
        # The kth smallest element is found in the root of a min heap of size k
        self.k = k

        # Keep popping from the min heap until its size is k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the value into the min heap
        heapq.heappush(self.minHeap, val)

        # Pop the min heap to compensate and make the heap size k again
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Return the new min value
        return self.minHeap[0]
