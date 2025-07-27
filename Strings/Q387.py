class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in s:
            if dic[i] == 1:
                return s.index(i)
                break
        return -1

