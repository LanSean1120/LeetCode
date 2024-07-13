class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        l = [[i, positions[i], healths[i], directions[i]] for i in range(len(positions))]
        l = sorted(l, key = lambda x:x[1])

        def func(stack, l):
            ######
            if not stack:
                stack.append(l)
                return stack
            
            temp = stack.pop()
            if temp[3] == "L" or l[3] == "R":
                stack.append(temp)
                stack.append(l)
                return stack

            elif temp[2] > l[2]:
                temp[2] -=1
                stack.append(temp)
                return stack
            elif temp[2] == l[2]:
                return stack
            else:
                l[2] -=1
                return func(stack, l)

        stack = deque()
        for i in range(len(l)):
            stack = func(stack, l[i])
        
        ans = list(stack)
        ans.sort()
        return [ans[i][2] for i in range(len(ans))]
