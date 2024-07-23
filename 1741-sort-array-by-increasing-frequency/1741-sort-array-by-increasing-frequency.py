class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def compare(x, y):
            if nums.count(x) > nums.count(y):
                return 1
            elif nums.count(x) < nums.count(y):
                return -1
            else:
                return y-x
        return sorted(nums, key = cmp_to_key(compare))