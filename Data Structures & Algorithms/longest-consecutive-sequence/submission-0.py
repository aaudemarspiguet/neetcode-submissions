class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()
        for n in nums:
            num_set.add(n)
        
        max_len = 0
        for n in nums:
            curr_len = 1
            while n + 1 in num_set:
                curr_len += 1
                n = n + 1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
