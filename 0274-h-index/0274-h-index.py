class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        while len(citations) >=h:
            h+=1
            citations = [val for val in citations if val >=h]
        return h-1

        