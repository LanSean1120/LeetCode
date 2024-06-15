class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        final = w
        menu = [[profits[i], capital[i]] for i in range(len(capital))]
        menu.sort()
        menu = menu[::-1]
        while k>0:
            nfinds = True
            for i in range(len(menu)):
                if menu[i][1]<=w:
                    final += menu[i][0]
                    w+=menu[i][0]
                    k-=1
                    menu.pop(i)
                    nfinds = False
                    break
            if nfinds:
                break
        return final

