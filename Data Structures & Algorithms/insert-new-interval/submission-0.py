class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #for loop length of interval:
            # no overlap 
             # if new_start > prev_end and new_end < next_start
             # add between prev and new

             # if overlap 
             # overlap bewteen 2 intervals
             # if new_start <= prev_end and new_end >= next start
             # return (prev_start, next_end)

             #other case 
             # if its just overlap between a single interval for before
             # if new_start >= prev_start and new end <= prev_end:
             # return prev
             # [1,4], [5, 6]
             # insert: [2, 3]
             # [1, 4], [5, 6]
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
        
