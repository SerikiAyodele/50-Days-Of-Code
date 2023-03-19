class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "./":
                continue
            elif stack and i=="../":
                stack.pop()
            elif i!="../":
                stack.append(i)
        return len(stack)