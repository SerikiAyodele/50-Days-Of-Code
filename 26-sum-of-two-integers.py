#Given two integers a and b, return the sum of the two integers without using the operators + and -.

#meduim
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            tmp = (a&b) << 1
            a = a^b
            b = tmp
        return  a&mask if b>mask else a

        # faster way around ;) 
        # return sum([a,b])