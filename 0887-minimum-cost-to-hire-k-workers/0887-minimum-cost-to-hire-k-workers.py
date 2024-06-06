class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        heap = []
        ans = float('inf')
        quality_sum = 0
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q
            
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            
            if len(heap) == k:
                ans = min(ans, quality_sum * ratio)
        return ans