class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        ans = 0
        times = minutesToTest // minutesToDie
        while (times+1)**ans < buckets:
            ans+=1
        return ans