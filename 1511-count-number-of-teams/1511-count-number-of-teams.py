class Solution:
    def numTeams(self, rating: List[int]) -> int:
        de_l = []
        in_l = []
        de_r = []
        in_r = []
        for i in range(len(rating)):
            increase = 0
            decrease = 0
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    decrease += 1
                elif rating[j] > rating[i]:
                    increase += 1
            de_r.append(decrease)
            in_r.append(increase)
        
        for i in range(len(rating)):
            increase = 0
            decrease = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    increase += 1
                elif rating[j] > rating[i]:
                    decrease += 1
            de_l.append(decrease)
            in_l.append(increase)

        ans = 0
        for i in range(len(rating)):
            ans += de_l[i] * de_r[i]
            ans += in_l[i] * in_r[i]
            
        return ans
