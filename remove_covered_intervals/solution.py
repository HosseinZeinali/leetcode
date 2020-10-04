class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        covered = set()
        k = 0
        for i in intervals:
            l = 0
            for j in intervals:
                if l > k:
                    if (j[0] >= i[0] and j[1] <= i[1]):
                        covered.add(l)
                l = l+1
            k = k + 1

        return len(intervals) - len(covered)
intervals = [[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]

solution = Solution()
x = solution.removeCoveredIntervals(intervals)
print(x)