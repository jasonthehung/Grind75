class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left, right = [], []

        for cur_start, cur_end in intervals:
            if cur_end < start:
                left.append([cur_start, cur_end])
            elif end < cur_start:
                right.append([cur_start, cur_end])
            else:
                start = min(start, cur_start)
                end = max(end, cur_end)

        return left + [[start, end]] + right
