from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap (key: int, value: frequency)
        # sort by keys by frequency and return the first k

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        
        sorted_keys = sorted(freq.keys(), key=freq.get, reverse=True)

        return sorted_keys[:k]
