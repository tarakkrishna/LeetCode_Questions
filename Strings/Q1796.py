class Solution(object):
    def secondHighest(self, s):
        x = []
        m1, m2 = float('-inf'), float('-inf')
        for i in s:
            if i.isdigit():
                x.append(int(i))
        x = list(set(x))
        for i in x:
            if i > m1:
                m2 = m1
                m1 = i
            elif i > m2:
                m2 = i
        if m2 == float('-inf'):
            return -1
        else:
            return m2
