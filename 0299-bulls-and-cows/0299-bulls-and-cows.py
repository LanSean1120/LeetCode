class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        seen =[]
        B_l = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A+=1
            else:
                seen.append(secret[i])
                B_l.append(guess[i])
        char = set(B_l)
        B = 0
        for elem in char:
            B += min(seen.count(elem), B_l.count(elem))
        
        return str(A) + "A" + str(B) + "B"