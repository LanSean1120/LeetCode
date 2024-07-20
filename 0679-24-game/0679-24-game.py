class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def generate(a, b):
            res = [a*b, a+b, a-b,b-a]
            if a!=0:
                res.append(b/a)
            if b!=0:
                res.append(a/b)
            return res
        
        def sol(cards):
            if len(cards)==1:
                return abs(cards[0] - 24.0)<0.001
            
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    for num in generate(cards[i], cards[j]):
                        Next = [num]
                        for k in range(len(cards)):
                            if k==i or k==j:
                                continue
                            Next.append(cards[k])
                        if sol(Next):
                            return True
            return False
        return sol(cards)