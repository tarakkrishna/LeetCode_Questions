s='iamtarak'
def reverseString(s):
    for i in range(len(s)):
        s.insert(i)=s.pop()
    return s
print(reverseString(s))