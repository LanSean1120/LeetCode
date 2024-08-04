class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subsum = []
        p_sum = [0]
        for i in range(n):
            p_sum.append(p_sum[-1] + nums[i])

        for i in range(len(p_sum)):
            for j in range(i+1, len(p_sum)):
                subsum.append(p_sum[j] - p_sum[i])
        
        subsum.sort()
        return sum(subsum[left-1:right])%(10**9+7)
        