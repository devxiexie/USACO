file=open('speeding.in', 'r')
out = open("speeding.out", "w")
n,m = map(int, file.readline().split())
limit=[]
bspeed=[]
for i in range(n):
    length,sl = map(int, file.readline().split())
    new=[sl]*length
    limit+=new
for i in range(m):
    length,sl = map(int, file.readline().split())
    new=[sl]*length
    bspeed+=new
ans=0
for i in range(100):
    ans=max(ans,bspeed[i]-limit[i])
out.write(str(ans))
file.close()
out.close()
