# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                 if nums[i] == nums[j] and i < j:
                     count += 1
        return count

        # d = {}
        # res = 0
        # for n in nums:
        #     if n in d:
        #         res += d[n]
        #         d[n] += 1
        #     else:
        #         d[n] = 1
        # return res