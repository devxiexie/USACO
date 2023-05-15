file=open('pails.in', 'r')
out = open("pails.out", "w")
x,y,m = map(int, file.readline().split())
xmax=int(m/x)
ymax=int(m/y)
high=0
for i in range(xmax+1):
    for j in range(ymax+1):
        total=i*x+j*y
        if total>m:
            continue
        high=max(high,total)
out.write(str(high))
file.close()
out.close()
