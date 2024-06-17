class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(c**(1/2))+1 if c**(1/2)%1!=0 else int(c**(1/2))
        while start <=end:
            if start**2 + end**2 ==c:
                return True
            elif start**2 + end**2 >c:
                end-=1
            else:
                start +=1
        
        return False