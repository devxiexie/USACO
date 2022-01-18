file=open('photo.in', 'r')
out = open("photo.out", "w")
n=int(file.readline())
b= [int(x) for x in file.readline().split()]
print('aaaaaaaaaa')
pos=[]
for i in range(1,n):
    a=[]
    used=[]
    a.append(i)
    for j in range(len(b)):
        x=b[j]-a[j]
        a.append(x)
    pos.append(a)
print(pos)
for i in range(len(pos)):
    hasmorethanone=len(set(pos[i])) < len(pos[i])
    contains0= 0 in pos[i]
    negs=[x for x in pos[i] if x < 0]
    if (not contains0) and (not hasmorethanone) and (not negs):
        print(*pos[i])
        out.write(' '.join(str(x) for x in pos[i]))
        break
file.close()
out.close()
