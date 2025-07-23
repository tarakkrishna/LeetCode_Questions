x=[1,2,3]
s=[]
res=''.join(map(str,x))
res=int(res)+1
for i in str(res):
    s.append(i)
print(s)