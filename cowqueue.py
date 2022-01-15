file=open('cowqueue.in', 'r')
n=int(file.readline())
ent=[]
dur=[]
pross=[0]*n

for i in range(n):
    arr = [int(x) for x in file.readline().split()]
    ent.append(arr[0])
    dur.append(arr[1])
tot=0

for a in range(n):
    nextent=-1
    for i in range(n):
        if(not pross[i] and (nextent==-1 or ent[i]<ent[nextent])):
            nextent=i
    pross[nextent]=True
    if(ent[nextent]>tot):
        tot=ent[nextent]+dur[nextent]
    else:
        tot=tot+dur[nextent]
    
out = open("cowqueue.out", "w")
out.write(str(tot))
out.close()
file.close()
