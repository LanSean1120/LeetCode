class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int m: down
        :type n: int n: right
        :rtype: int
        """
        f = {}
        def sol(r,l):
            if r ==1 or l==1:
                return 1
            if tuple([r,l]) in f:
                return f[tuple([r,l])]
            else:
                f[tuple([r,l])] = sol(r-1, l) + sol(r,l-1)
                return f[tuple([r,l])]

        return sol(m,n)
        