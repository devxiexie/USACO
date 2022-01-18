file=open('cowtip.in', 'r')
out=open("cowtip.out", "w")
n=int(file.readline())
cows=[]
for i in range(n):
    arr = file.readline().strip()
    arr=list(map(int, arr))
    cows.append(arr)
trys=0
for i in reversed(range(n)):
    for j in reversed(range(n)):
        print(cows)
        if cows[i][j]==1:
            for a in range(i+1):
                for b in range(j+1):
                    if cows[a][b]==0:
                        cows[a][b]+=1
                    else:
                        cows[a][b]=0
                    
            trys+=1
print(trys)
out.write(str(trys))
out.close()
file.close()
