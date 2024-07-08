class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        start = 0
        while len(friends) >1:
            t = (k-1)%len(friends)
            j = (start + t)%len(friends)
            friends.pop((start + t)%len(friends))
            start = (j)%len(friends)
        return friends[0]