class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(x):
            dist = 0
            m_temp = m
            for i in range(1,len(position)):
                dist += position[i] - position[i-1]
                if dist >=x:
                    dist = 0
                    m_temp -=1
                if m_temp <=1:
                    return True
            if m_temp <=1:
                return True
            else:
                return False
        
        position.sort()
        
        left, right = 0, position[-1]-position[0]
        while left+1<right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid
            else:
                right = mid-1
        return right if check(right) else left