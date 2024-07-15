class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            stack = deque()
            for i in range(len(string)):
                if string[i] == "(":
                    stack.append(string[i])
                elif string[i] == ")":
                    if stack:
                        stack.pop()
                    else:
                        return False
            if not stack:
                return True
            return False
        def create_child(l: list):
            res = []
            for i in range(len(l)):
                for j in range(len(l[i])):
                    if l[i][j] == "(" or l[i][j] == ")":
                        res.append(l[i][:j]+l[i][j+1:])
            return list(set(res))
        finds = False
        ans = []
        s = [s]
        while not finds:
            for elem in s:
                if is_valid(elem):
                    finds = True
                    ans.append(elem)
            s = create_child(s)
        return ans


