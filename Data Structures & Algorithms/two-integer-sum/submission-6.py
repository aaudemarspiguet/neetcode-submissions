class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if other in num_dict and num_dict[other] != i:
                return [num_dict[other], i]
            num_dict[nums[i]] = i
            
        return []
        
