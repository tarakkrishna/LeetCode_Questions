s='leetcode'
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print(s.index(i))
        break
    else:
        print(-1)

