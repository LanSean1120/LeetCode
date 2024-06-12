class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 =0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                n0+=1
            elif nums[i] == 1:
                n1 +=1
            else:
                n2+=1
        N = len(nums)
        for n in range(n0):
            nums.remove(0)
            nums.append(0)
        for n in range(n1):
            nums.remove(1)
            nums.append(1)
        for n in range(n2):
            nums.remove(2)
            nums.append(2)