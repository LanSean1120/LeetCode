class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        count = defaultdict(int)
        for i, j, a, b in rectangles:
            count[(i, j)] += 1
            count[(a, b)] += 1
            count[(a, j)] += 1
            count[(i, b)] += 1
        rectangles.sort()
        a = min([elem[0] for elem in rectangles])
        b = min([elem[1] for elem in rectangles])
        c = max([elem[2] for elem in rectangles])
        d = max([elem[3] for elem in rectangles])
        corner1 = (a, b)
        corner2 = (a, d)
        corner3 = (c, b)
        corner4 = (c, d)

        for key in count:
            if key == corner1 or key == corner2 or key == corner3 or key == corner4:
                if count[key] !=1:
                    return False
            else:
                if count[key]%2 != 0:
                    return False
        
        cover = 0
        for elem in rectangles:
            cover += (elem[2] - elem[0]) * (elem[3] - elem[1])
        if cover != (c-a)*(d-b):
            return False
        return True
        