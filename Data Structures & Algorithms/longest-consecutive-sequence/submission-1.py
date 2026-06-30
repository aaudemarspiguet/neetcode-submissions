class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n) to convert list into hash set
        num_set = set(nums)
        
        max_len = 0
        for n in nums: # O(n) to iterate
            curr_len = 1
            while n + 1 in num_set: # hash set lookup is O(1)
                curr_len += 1
                n = n + 1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
