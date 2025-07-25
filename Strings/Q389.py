class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if i not in s:
                return i
                break
            else:
                if s.count(i) != t.count(i):
                    return i
                    break

