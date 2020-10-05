class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        print(intervals)
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

    def removeCoveredIntervals2(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        uncovereds = []
        uncovereds.append(intervals[0])
        for i in intervals[1:]:
            is_covered = False
            for u in uncovereds:
                if i[1] <= u[1]:
                    is_covered = True
            if is_covered == False:
                uncovereds.append(i)

        return len(uncovereds)

intervals =   [[1,4],[3,6],[2,8]]

solution = Solution()
x = solution.removeCoveredIntervals2(intervals)
print(x)