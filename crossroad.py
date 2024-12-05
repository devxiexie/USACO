file=open('crossroad.in','r')
n=int(file.readline())
sights=[0]*11
ans=0
for i in range(n):
    cow,side= map(int, file.readline().split())
    side+=1
    if sights[cow]>0 and sights[cow]!=side:
        ans+=1
    sights[cow]=side
print(ans)
o=open('crossroad.out','w')
o.write(str(ans))
o.close()
file.close()
