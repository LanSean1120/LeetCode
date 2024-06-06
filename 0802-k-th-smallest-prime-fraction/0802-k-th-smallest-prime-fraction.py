class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        f = []
        arr.sort()
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                f.append([arr[i]/arr[j], [arr[i], arr[j]]])
        f.sort()
        return f[k-1][1]
    
        

        