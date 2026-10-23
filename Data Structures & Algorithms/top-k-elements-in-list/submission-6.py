from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))  # min heap arranges the dict value wrt to the first element
            else:
                heapq.heappushpop(heap,(value, key))
        
        return [h[1] for h in heap]

        