class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count

#example usage
solution = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(solution.eraseOverlapIntervals(intervals))
