class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        f = {}
        for i in range(len(points)-1):
            g={}
            for j in range(i+1, len(points)):
                if points[i][1]-points[j][1] !=0:
                    if (float(points[i][0]-points[j][0])/float(points[i][1]-points[j][1])) not in g:
                        g[(float(points[i][0]-points[j][0])/float(points[i][1]-points[j][1]))] =2
                    else:
                        g[(float(points[i][0]-points[j][0])/float(points[i][1]-points[j][1]))]+=1
                else:
                    if "-" not in g:
                        g["-"] = 2
                    else:
                        g["-"] +=1
            for elem in g:
                if elem not in f:
                    f[elem] = g[elem]
                else:
                    f[elem] = max(f[elem], g[elem])
        if len(points) ==1:
            return 1
        return max(f.values())

        