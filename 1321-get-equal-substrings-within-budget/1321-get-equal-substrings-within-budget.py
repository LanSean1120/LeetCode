class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        '''
        ans = [0]
        start = 0
        end = 0
        cost = maxCost
        while end < len(s):
            if abs(ord(s[end])-ord(t[end])) <= cost:
                cost -= abs(ord(s[end])-ord(t[end]))
                if end == len(s)-1:
                    ans.append(end - start+1)
                end +=1
                
            else:
                ans.append(end - start)
                start +=1
                end = start
                cost = maxCost
        return max(ans)
'''
        l = [abs(ord(s[end])-ord(t[end])) for end in range(len(s))]
        start = 0
        end = 0
        cost = maxCost
        ans = []
        while end<len(s):
            if l[end] <= cost:
                cost -= l[end]
                if end == len(s)-1:
                    ans.append(end-start+1)
                end+=1
            elif end<start:
                end = start
                cost = maxCost
            else:
                ans.append(end-start)
                cost += l[start]
                start +=1
        return max(ans)