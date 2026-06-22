class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # break it down into two problems:
        # product of elements to the left of i, and right of i
        # so compute two arrays: prefix and suffix,
        # solution at i, becomes prefix[i-1] * suffix[i+1]

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)

        # make prefix array
        prefix[0] = nums[0]
        for i in range(1, len(nums), +1):
            prefix[i] = prefix[i - 1] * nums[i]

        # make suffix array
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * suffix[i + 1]

        return output




