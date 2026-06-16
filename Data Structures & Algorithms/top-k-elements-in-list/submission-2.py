class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict: dict = {}

        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 0
            freq_dict[n] += 1
        
        new_list = list(freq_dict.keys())
        new_list.sort(key = freq_dict.get) # turn keys into list and sort by value

        return new_list[-k:]
            
            
        