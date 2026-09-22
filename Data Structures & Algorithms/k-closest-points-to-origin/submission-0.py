class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for x, y in points:
            d = x * x + y * y
            heapq.heappush(heap,(-d, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        return[[x, y] for _, x, y in heap]