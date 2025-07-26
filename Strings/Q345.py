class Solution(object):
    def reverseVowels(self, s):

        v = ['a', 'e', 'i', 'o', 'u']
        rev = []
        ss = []
        for i in s:
            if i.lower() in v:
                rev.append(i)
            ss.append(i)
        for i in range(len(ss)):
            if ss[i].lower() in v:
                ss[i] = rev[-1]
                rev.pop()
        return ''.join(ss)

