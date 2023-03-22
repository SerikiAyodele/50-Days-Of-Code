class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1]<heights[i]:
                stack.pop()
            if not stack:
                res.append(i)
            stack.append(heights[i])
            
        return res[::-1]