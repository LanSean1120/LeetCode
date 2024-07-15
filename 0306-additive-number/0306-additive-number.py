class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <3:
            return False
        def is_valid(l: list, v1: str, v2: str):
            if (v1[0] == "0" and len(v1)>1) or (v2[0] == "0" and len(v2)>1):
                return False
            
            quene = deque(l[::-1])
            while  quene:
                curr = str(int(v1) + int(v2))
                for i in range(len(curr)):
                    if quene:
                        temp = quene.pop()
                        if temp != curr[i]:
                            return False
                    else:
                        return False
                v1 = v2
                v2 = curr
            return True

        for i in range(1, len(num)-1):
            for j in range(1, len(num) - i):
                if is_valid([num[k] for k in range(i+j, len(num))], num[:i], num[i:i+j]):
                    return True

        return False
                
