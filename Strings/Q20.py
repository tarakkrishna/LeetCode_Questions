class Solution(object):
    def isValid(self, s):
        stack=[]
        open=['(','{','[']
        dic={ ')': '(', '}': '{', ']': '[' }
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if not(not stack) and stack[-1]==dic[i]:
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        else:
            return False