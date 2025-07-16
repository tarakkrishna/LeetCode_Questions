arr=[1,2,3,4,4]
arr1=[4,5,6,6]
a=set(arr)-set(arr1)
b=set(arr1)-set(arr)
answer=[[],[]]
answer[0]=list(a)
answer[1]=list(b)
print(answer)