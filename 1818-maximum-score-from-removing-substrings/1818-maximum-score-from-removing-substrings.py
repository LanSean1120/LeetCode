class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def check_ab(n: int, curr: str):
            stack = deque()
            m = n
            for i in range(len(curr)):
                if stack:
                    if curr[i] == "b":
                        temp = stack.pop()
                        if temp == "a":
                            n += x
                        else:
                            stack.append(temp)
                            stack.append(curr[i])
                    else:
                        stack.append(curr[i])
                else:
                    stack.append(curr[i])
            curr = list(stack)
            if m!=n:
                return check_ab(n, curr)
            else: 
                return [n, curr]
        
        def check_ba(n: int, curr: str):
            stack = deque()
            m = n
            for i in range(len(curr)):
                if stack:
                    if curr[i] == "a":
                        temp = stack.pop()
                        if temp == "b":
                            n += y
                        else:
                            stack.append(temp)
                            stack.append(curr[i])
                    else:
                        stack.append(curr[i])
                else:
                    stack.append(curr[i])
            curr = list(stack)
            if m!=n:
                return check_ba(n, curr)
            else: 
                return [n, curr]
        
        if x>=y:
            n, s = check_ab(0, s)
            return check_ba(n, s)[0]
        else:
            n, s = check_ba(0, s)
            return check_ab(n, s)[0]

