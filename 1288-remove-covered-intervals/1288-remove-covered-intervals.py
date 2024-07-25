class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        prev_end = 0

        for start, end in intervals:
            # If the current interval is not covered by the previous interval
            if end > prev_end:
                count += 1
                prev_end = end

        return count