class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [[heights[i], names[i]] for i in range(len(heights))]
        l.sort()
        l = l[::-1]
        return [l[i][1] for i in range(len(l))]