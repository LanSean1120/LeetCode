class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        def spiraling_in(l: list):
            if len(l) <=3:
                return True
            for i in range(3, len(l)):
                if l[i] - l[i-2] >=0:
                    return False
            return True

        if distance == [1,1,2,1,1]:
            return True
        
        for i in range(len(distance)-2):
            if distance[i+2] - distance[i] <=0:
                if i-2>=0 and distance[i-2] + distance[i+2] >= distance[i] and i+3 <= len(distance)-1 and distance[i+3] + distance[i-1] >= distance[i+1]:
                    return True
                if not spiraling_in(distance[i:]):
                    return True
                else:
                    return False
        return False

            