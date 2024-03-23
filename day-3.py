n=12467
while n>0:
    digit=n%10
    print(digit)
    n=n//10

n=12345
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
    print(s)

n=12345
count=0
while n>0:
    n=n//10
    count=count+1
print(count)

n=12467
count=0
while n>0:
    d=n%10
    if d%2==0:
        c=c+1
        n=n//10
        print(n)

n=12
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
    if s>n:
        print("true")
else:
    print("false")