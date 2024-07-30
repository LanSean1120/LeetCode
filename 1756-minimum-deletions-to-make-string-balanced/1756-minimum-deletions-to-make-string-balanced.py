class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0
        count_a = 0
        count = []
        for i in range(len(s)):
            if s[i] == "b":
                count.append(count_b)
                count_b += 1
        count.append(count_b)
        j = len(count)-2
        s = s[::-1]
        for i in range(len(s)):
            if s[i] == "b":
                count[j] += count_a
                j-=1
            else:
                count_a+=1

        return min(count)

        