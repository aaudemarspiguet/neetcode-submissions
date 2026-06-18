class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                return True
        return False