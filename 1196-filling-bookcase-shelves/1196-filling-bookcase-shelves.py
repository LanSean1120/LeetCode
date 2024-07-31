class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [int()]*n

        def sol(i):
            if not i < n:
                return 0
            if dp[i]:
                return dp[i]
            if i == n-1:
                return books[i][1]
            
            candi = []
            k = i
            maxx = books[k][1]
            s = shelfWidth - books[k][0]
             
            while k < n and s >=0:
                candi.append(maxx+sol(k+1))
                k+=1
                if k<n:
                    s-=books[k][0]
                    if books[k][1] > maxx:
                        maxx = books[k][1]

            dp[i] = min(candi)
            return dp[i]
        
        return sol(0)


