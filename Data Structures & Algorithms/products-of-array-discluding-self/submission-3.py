class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute two arrays (prefix and suffix products each in O(n) time)
        # for each element, the product without itself is simply prefix[i - 1] * suffix[i + 1]

        if len(nums) == 0:
            return nums
        
        sol = [1] * len(nums)
        
        prefix = [1] * len(nums)
        prefix[0] = nums[0] # populate first element, to eliminate repeated checks
        for i in range(1, len(nums), +1):
            prefix[i] = prefix[i - 1] * nums[i]
        
        suffix = [1] * len(nums)
        suffix[-1] = nums[-1] # populate first element, to eliminate repeated checks
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        # compute product except self
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                sol[i] = prefix[i - 1] * suffix[i + 1]
            elif i == 0:
                sol[i] = suffix[i + 1]
            else:
                sol[i] = prefix[i - 1]
            
        return sol


            
