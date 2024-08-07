class Solution:
    def minimumPushes(self, word: str) -> int:
        l = Counter(word)
        l = [val for val in l.values()]
        l.sort(reverse = True)

        i = 1
        j = 1
        ans = 0
        for val in l:
            ans += val * j
            if i==8:
                j+=1
                i = 1
            else:
                i+=1
        return ans
