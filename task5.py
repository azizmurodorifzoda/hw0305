a=int(input())
b=0
while a>0:
    res=a%10
    b=b*10+res
    print(b)
    a=a//10