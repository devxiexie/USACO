file=open('shuffle.in', 'r')
out = open("shuffle.out", "w")
n=int(file.readline())
shuffle = [int(x) for x in file.readline().split()]
ids=[int(x) for x in file.readline().split()]
for i in range(3):
    newid=[0]*n
    for j in range(n):
        shufindex=shuffle.index(j+1)
        newid[shufindex]=ids[j]
    ids=newid
    print(ids)
for i in range(n):
    out.write(str(ids[i])+'\n')
out.close()
file.close()
