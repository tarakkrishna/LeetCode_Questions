x=121
def pal(x):
    y = str(x)[::-1]
    if int(x) == int(y):
        return True
    else:
        return False

if pal(x) != True:
    print('not pal')
else:
    print('pal')