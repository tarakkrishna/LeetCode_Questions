class Solution(object):
    def daysBetweenDates(self, date1, date2):
        from datetime import *
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.strptime(date2, '%Y-%m-%d')
        diff = abs(date2 - date1)
        return diff.days
