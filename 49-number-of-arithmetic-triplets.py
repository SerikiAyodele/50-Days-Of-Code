class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n = len(nums)
        count = 0
        i, j, k = 0, 1, 2
        while i < n and j < n and k < n:
            if nums[j] - nums[i] < diff:
                j += 1
            elif nums[j] - nums[i] > diff:
                i += 1
            else:
                if nums[k] - nums[j] < diff:
                    k += 1
                elif nums[k] - nums[j] > diff:
                    j += 1
                else:
                    count +=1
                    k += 1
        return count
    
    