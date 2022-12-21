class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # hashmap={}
        # answer = []

        # if i in nums:
        #     if nums in hashmap:
        #         n = 1
        #         ans = n *= nums[i]
        
            
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res