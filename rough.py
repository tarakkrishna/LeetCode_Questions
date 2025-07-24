s='()[]'
close=[')','}',']']
dic={ ')': '(', '}': '{', ']': '[' }
open=[]
for i in s:
    if i not in close:
        open.append(i)
for i in s:
    if i==dic[i]:
        open.remove(open[0])
    else:
        print('False')
print('True')