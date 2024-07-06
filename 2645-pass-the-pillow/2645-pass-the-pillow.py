class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        ans = 1
        adj = -1
        while time >0:
            if ans == 1 or ans == n:
                adj*=-1
            ans += adj
            time -=1
        return ans
        
        
        