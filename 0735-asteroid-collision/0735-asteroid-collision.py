class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        def func(stack, n:int):
            if not stack:
                stack.append(n)
                return stack
            temp = stack.pop()
            if temp <0:
                stack.append(temp)
                stack.append(n)
                return stack

            if temp + n>0:
                stack.append(temp)
                return stack
            elif temp + n ==0:
                return stack
            else:
                return func(stack, n)

        for i in range(len(asteroids)):
            if stack:
                temp = stack.pop()
                if temp < 0:
                    stack.append(temp)
                    stack.append(asteroids[i])
                    continue

                if asteroids[i] >0:
                    stack.append(temp)
                    stack.append(asteroids[i])
                else:
                    stack.append(temp)
                    stack = func(stack, asteroids[i])
            else:
                stack.append(asteroids[i])

        return list(stack)