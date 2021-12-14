n=int(input())
petals=input()
petals=petals.split()
integer_map = map(int, petals)
petals = list(integer_map)
ans=0
for i in range(n):
    for j in range(i,n):
        totalpetals=0
        for k in range(i,j+1):
            totalpetals+=petals[k]
        average=False
        for k in range(i,j+1):
            if(totalpetals==petals[k]*(j-i+1) ):
                average=True
                #print(i+1,j+1)
        if(average):
            ans+=1
