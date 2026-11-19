class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a heap
        maxHeap = []

        # For every point
        for x, y in points:
            # Calculate the distance and make it neg to make it max heap
            # No need to square root x^2 + y^2 because taking the sqrt changes the distance vals
            # but preserves their order of smallest distances
            dist = -(x ** 2 + y ** 2)

            # Add the distance and its respective point to the max heap
            heapq.heappush(maxHeap, (dist, x, y))

            # Pop if the length is more than k
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        # As you keep popping, add the points to the result until theres no more values in the max heap
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])

        return res