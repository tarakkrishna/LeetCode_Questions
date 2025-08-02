s = "abc1111"
x = []
m1, m2 = float('-inf'), float('-inf')
for i in s:
    if i.isdigit():
        x.append(int(i))
for i in x:
    if i > m1:
        m2 = m1
        m1 = i
    elif i > m2:
        m2 = i
if m2 == float('-inf'):
    print(-1)
else:
    print(m2)
