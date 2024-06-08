class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l = [0]
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            l.append(val%k)

        d = defaultdict(list)
        for i in range(len(l)):
            d[l[i]].append(i)
        for key in d:
            elem = d[key]
            if max(elem) - min(elem)>=2:
                return True
        return False