class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N=nums[0]
        for i in range(1,len(nums)):
            N^=nums[i]

        n = bin(N)[2:]
        k = bin(k)[2:]
        n = n[::-1]
        k=k[::-1]
        ans = 0
        for j in range(max(len(n), len(k))):
            if j<len(n) and j<len(k) and n[j] !=k[j]:
                ans +=1
            elif j>=len(n) and k[j] !="0":
                ans +=1
            elif j>=len(k) and n[j] !="0":
                ans +=1
        return ans
        