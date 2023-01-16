n=int(input())
x=[]
x=(list(map(int, input().split())))


o=0
e=0
a=0
c=len(x)
for i in range(n):
    if (x[a] % 2) == 0:  
        e=e+1
    else:
        o=o+1
    a+=1
if e==o or e==o+1:
    print(len(x))
if e>o+1:
    print(2*o + 1)
if e<o:
    for i in range(1010):
        o=o-2
        e=e+1
        c=c-1
        if e >= o:
            print(2*o+1)
            break 
