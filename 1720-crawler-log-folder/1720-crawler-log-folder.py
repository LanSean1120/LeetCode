class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in range(len(logs)):
            if logs[i] == './':
                continue
            elif logs[i] == '../':
                ans = max(0, ans-1)
            elif logs[i] == 'x/':
                ans += 1
            else:
                ans+=1
        return ans