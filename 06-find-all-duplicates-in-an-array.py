# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []

        for i in nums:
            if i in s:
                ans.append(i)
            s.add(i)
        return ans