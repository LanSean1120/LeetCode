class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        if len(nums)>=k:
            self.l = sorted(nums)[len(nums)-k:]
        else:
            self.l = []

    def add(self, val: int) -> int:
        self.nums.append(val)
        if not self.l:
            self.l = sorted(self.nums)[len(self.nums)-self.k:]
            return self.l[0]

        if val<=self.l[0]:
            return self.l[0]
        else:
            self.l.pop(0)
            insort(self.l, val)
            return self.l[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)