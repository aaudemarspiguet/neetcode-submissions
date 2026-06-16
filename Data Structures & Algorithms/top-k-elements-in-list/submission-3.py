from heapq import heappush, heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # priority queue solution
        sol = []

        # build buckets
        freq_dict: dict = {}
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 0
            freq_dict[n] += 1
        
        # build max heap from buckets
        heap = []
        for key, val in freq_dict.items():
            heappush(heap, (-val, key)) # orders items by largest to smallest

        for key in range(k):
            sol.append(heappop(heap)[1])

        return sol

        