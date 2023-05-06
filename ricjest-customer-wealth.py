class solution:
    def maxwealth(self, accounts: list[list[int]]):
        maxwealth=0

        for i in range(len(accounts)):
            totalwealth = sum(accounts[i])
            maxwealth = max(maxwealth,totalwealth)
            return maxwealth