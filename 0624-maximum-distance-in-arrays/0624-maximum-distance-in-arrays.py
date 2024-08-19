class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        minn = min(arrays[0])
        maxx = max(arrays[0])
        for i in range(1, len(arrays)):
            temp_minn = min(arrays[i])
            temp_maxx = max(arrays[i])
            ans = max(ans, temp_maxx - minn, maxx - temp_minn)
            minn = min(minn, temp_minn)
            maxx = max(maxx, temp_maxx)

        return ans
