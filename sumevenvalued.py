limit = 4000000
a,b=1,2
total=0
while a<=limit :
    if a%2==0:
        total+=a
        a,b=b,a+b
        print("sum of even fabonacci terms below four million:",total)
