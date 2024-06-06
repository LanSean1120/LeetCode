class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s):
            if s==s[::-1]:
                return True
            else:
                return False
        
        memo = {}
        def sol(s):
            res = []
            if s in memo:
                return memo[s]
            if s=="":
                return [[]]
            if len(s)==1:
                return [[s]]

            for i in range(1, len(s)+1):
                temp=[]
                if check(s[:i]):
                    for j in range(len(sol(s[i:]))):
                        temp.append([s[:i]]+sol(s[i:])[j])
                res+=temp
            memo[s]=res
            return res
        return sol(s)

            