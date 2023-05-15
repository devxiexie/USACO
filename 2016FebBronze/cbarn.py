file=open('cbarn.in', 'r')
out=open('cbarn.out', 'w')
n=int(file.readline())
cows=[]
for i in range(n):
    cows.append(int(file.readline()))
ans=n*n*100
for i in range(n):
    dis=0
    for j in range(n):
        dis+=cows[(i+j)%n]*j
    ans=min(ans,dis)
print(ans)
out.write(str(ans))
out.close()
