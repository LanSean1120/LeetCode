class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0]=1
        '''"P", "L", "A"'''
        for i in range(1, n+1):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2])%(10**9+7)
            '''+"A" and +"P"'''
            dp[i][1][0] = (dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2]+dp[i-1][1][0]+dp[i-1][1][1]+dp[i-1][1][2])%(10**9+7)
            '''+"L"'''
            dp[i][0][1] = dp[i-1][0][0]%(10**9+7)
            dp[i][1][1] = dp[i-1][1][0]%(10**9+7)
            dp[i][0][2] = dp[i-1][0][1]%(10**9+7)
            dp[i][1][2] = dp[i-1][1][1]%(10**9+7)
        
        ans = 0 
        for i in range(2):
            for j in range(3):
                ans += dp[n][i][j]
        return ans%(10**9+7)

