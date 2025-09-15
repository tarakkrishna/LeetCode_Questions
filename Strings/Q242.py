class Solution(object):
    def isAnagram(self, s, t):
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False
