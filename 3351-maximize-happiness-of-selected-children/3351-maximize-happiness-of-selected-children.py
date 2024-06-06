class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness.sort()
        happiness = happiness[::-1]
        happiness = happiness[:k]
        for i in range(len(happiness)):
            if happiness[i] - i > 0:
                ans += happiness[i] - i
            else:
                break
        return ans
