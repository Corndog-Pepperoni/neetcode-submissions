class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a heap with vals containing the points distance from the origin and the points
        # x and y themselves
        # No need to square root x^2 + y^2 because taking the sqrt changes the distance vals
        # but preserves their order of smallest distances
        heap = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(heap)

        # Initialize the result
        res = []
        
        # Add the k closest points to the result
        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
