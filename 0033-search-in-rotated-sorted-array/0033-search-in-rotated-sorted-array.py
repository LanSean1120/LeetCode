class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = {elem: index for index, elem in enumerate(nums)}
        if target in nums:
            return dic[target]
        else: return -1