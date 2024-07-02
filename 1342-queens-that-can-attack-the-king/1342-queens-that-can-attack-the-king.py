class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        #case 1
        i=1
        while king[0]+i<8:
            if [king[0]+i, king[1]] in queens:
                ans.append([king[0]+i, king[1]])
                break
            i+=1
        i=1
        while king[0]-i>=0:
            if [king[0]-i, king[1]] in queens:
                ans.append([king[0]-i, king[1]])
                break
            i+=1
        #case2
        i=1
        while king[1]+i<8:
            if [king[0], king[1]+i] in queens:
                ans.append([king[0], king[1]+i])
                break
            i+=1
        i=1
        while king[1]-i>=0:
            if [king[0], king[1]-i] in queens:
                ans.append([king[0], king[1]-i])
                break
            i+=1
        #case3
        i=1
        while king[0]+i<8 and king[1]+i<8:
            if [king[0]+i, king[1]+i] in queens:
                ans.append([king[0]+i, king[1]+i])
                break
            i+=1
        i=1
        while king[0]-i>=0 and king[1]-i>=0:
            if [king[0]-i, king[1]-i] in queens:
                ans.append([king[0]-i, king[1]-i])
                break
            i+=1
        #case4
        i=1
        while king[0]+i<8 and king[1]-i>=0:
            if [king[0]+i, king[1]-i] in queens:
                ans.append([king[0]+i, king[1]-i])
                break
            i+=1
        #case5
        i=1
        while king[0]-i>=0 and king[1]+i<8:
            if [king[0]-i, king[1]+i] in queens:
                ans.append([king[0]-i, king[1]+i])
                break
            i+=1
        
        return ans
