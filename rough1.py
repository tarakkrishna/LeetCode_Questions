s = "abcde"
goal = "cdeab"
s=list(s)
s[0],s[-1]=s[-1],s[0]
for i in s:
    if ''.join(s)==goal:
        print(True)
        break
print(False)
