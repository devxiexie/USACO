file = open("breedflip.in", "r")
n=int(file.readline())
ex=file.readline()
ex1=file.readline()
a=[]
a[:0]=ex
b=[]
b[:0]=ex1
past=False
ans=0
for i in range(n):
    if(a[i]!=b[i]):
        if(not past):
            past=True
            ans+=1
    else:
        past=False
output = open("breedflip.out", "w")
output.write(str(ans))
output.close()
file.close()
