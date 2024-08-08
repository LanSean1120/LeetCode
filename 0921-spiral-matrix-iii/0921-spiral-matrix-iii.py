class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dis = 1
        now_loca = [rStart, cStart]
        ans = [[rStart, cStart]]
        
        #the length of ans
        n = 1

        #keep going when no loca missing
        while n < rows * cols:
            if dis%2==1:
                for k in range(dis):
                    if 0 <= now_loca[1]+1 < cols and 0 <= now_loca[0] < rows:
                        ans.append([now_loca[0], now_loca[1]+1])
                        n+=1
                    now_loca[1] += 1
                    

                for k in range(dis):
                    if 0 <= now_loca[1] < cols and 0 <= now_loca[0]+1 < rows:
                        ans.append([now_loca[0]+1, now_loca[1]])
                        n+=1
                    now_loca[0] += 1
                    

            else:
                for k in range(dis):
                    if 0 <= now_loca[1]-1 < cols and 0 <= now_loca[0] < rows:
                        ans.append([now_loca[0], now_loca[1]-1])
                        n+=1
                    now_loca[1] -= 1
                    

                for k in range(dis):
                    if 0 <= now_loca[1] < cols and 0 <= now_loca[0]-1 < rows:
                        ans.append([now_loca[0]-1, now_loca[1]])
                        n+=1
                    now_loca[0] -= 1
                    
            dis+=1
        return ans