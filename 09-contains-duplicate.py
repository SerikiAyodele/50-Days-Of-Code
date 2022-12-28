#faster solution using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False


#using hasmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap= {}

        for i in nums:
            if i in hashmap:
                return True
            hashmap[i]=i
        return False