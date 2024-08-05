class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = set()
        notDistinct = set()
        for i in range(len(arr)):
            if arr[i] not in seen:
                seen.add(arr[i])
            else:
                notDistinct.add(arr[i])
        for i in range(len(arr)):
            if arr[i] not in notDistinct:
                if k==1:
                    return arr[i]
                else:
                    k-=1
        return ""