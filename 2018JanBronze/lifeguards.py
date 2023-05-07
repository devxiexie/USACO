file=open('lifeguards.in','r')
n=int(file.readline())
shifts=[]
for i in range(n):
    arr = [int(x) for x in file.readline().split()]
    shifts.append(arr)
def calc(shifts,miss):
    points=[0]*1000
    for i in range(len(shifts)):
        for j in range(shifts[i][0],shifts[i][1]):
            if i!=miss:
                points[j]=1
    x=points.count(1)
    return x
ans=0
file.close()
for a in range(n):
    tot=calc(shifts,a)
    ans=max(ans,tot)
print(ans)
o=open('lifeguards.out','w')
o.write(str(ans))
o.close()
