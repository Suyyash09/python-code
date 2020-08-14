n=int(input("enter the number upto which you want the fibo series:"))
a=0
b=1
count=1
sum=0

while count<=n:
    print(sum, end=",")
    count=count+1
    a=b
    b=sum
    sum=a+b
