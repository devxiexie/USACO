file=open('mowing.in', 'r')
n=int(file.readline())
x=0
y=0
beento=[]
ans=100000
for i in range(n):
    direc,dis = map(str, file.readline().split())
    dis=int(dis)
    if direc=='N':
        for j in range(dis):
            x+=1
            print(x,y)
            beento.append([x,y])
            now=[x,y]
            if beento.count(now)>1:
                ind=[]
                for (index, item) in enumerate(beento):
                    if item == now:
                        ind.append(index)
                e=ind[-1]-ind[-2]
                ans=min(ans,e)
    if direc=='S':
        for j in range(dis):
            x-=1
            print(x,y) 
            beento.append([x,y])
            now=[x,y]
            if beento.count(now)>1:
                ind=[]
                for (index, item) in enumerate(beento):
                    if item == now:
                        ind.append(index)
                e=ind[-1]-ind[-2]
                ans=min(ans,e)
    if direc=='E':
        for j in range(dis):
            y+=1
            print(x,y)
            beento.append([x,y])
            now=[x,y]
            if beento.count(now)>1:
                ind=[]
                for (index, item) in enumerate(beento):
                    if item == now:
                        ind.append(index)
                e=ind[-1]-ind[-2]
                ans=min(ans,e)
    if direc=='W':
        for j in range(dis):
            y-=1
            print(x,y)
            beento.append([x,y])
            now=[x,y]
            if beento.count(now)>1:
                ind=[]
                for (index, item) in enumerate(beento):
                    if item == now:
                        ind.append(index)
                e=ind[-1]-ind[-2]
                ans=min(ans,e)
if ans==100000:
    ans=-1
print(ans)
out=open('mowing.out', 'w')
out.write(str(ans))
out.close()
file.close()
