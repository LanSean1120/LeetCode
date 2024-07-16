class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        temp = []
        count = 0
        words = deque(words[::-1])

        while words:
            n = 0
            line_elem = []
            leng = 0
            while words:
                word = words.pop()
                if n + len(word) <= maxWidth:
                    line_elem.append(word)
                    n += len(word)
                    n += 1
                    leng += len(word)
                else:
                    words.append(word)
                    break
            line = ''

            if not words:
                for elem in line_elem:
                    line += elem
                    if len(line) < maxWidth:
                        line += " "
                line += " "*(maxWidth - len(line))
                ans.append(line)
                break

            if len(line_elem) == 1:
                line = line_elem[0] + " "*(maxWidth-len(line_elem[0]))
                ans.append(line)
                continue
            space = (maxWidth - leng)//(len(line_elem)-1)
            x = (maxWidth - leng)%(len(line_elem)-1)
            for i in range(len(line_elem)):
                line += line_elem[i]
                if i == len(line_elem)-1:
                    break
                if i<x:
                    line += " "*(space+1)
                else:
                    line += " "*space
            ans.append(line)
        
        return ans


