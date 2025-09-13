class Solution(object):
    def fizzBuzz(self, n):
        x=range(1,n+1)
        for i in list(x):
            if i%3==0 and i%5==0:
                x[i-1]="FizzBuzz"
            elif i%3==0:
                x[i-1]="Fizz"
            elif i%5==0:
                x[i-1]="Buzz"
        return list(map(str,x))