class Solution(object):
    def plusOne(self, digits):
        ans=[]
        res=''.join(map(str,digits))
        res=int(res)+1
        for i in str(res):
            ans.append(int(i))
        return ans