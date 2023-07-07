class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        hashtable = []
        total = 0

        for i in nums:
            total += i
            hashtable.append(total)
        return hashtable
    

    