file=open('gymnastics.in', 'r')
k,n = map(int, file.readline().split())
orders=[]
for i in range(k):
    arr = [int(x) for x in file.readline().split()]
    orders.append(arr)
print(orders)
answer=0
for i in range(n):
    for j in range(n):
        tot=0
        for a in range(k):
            if orders[a].index(i+1)>orders[a].index(j+1):
                tot+=1
        if tot==k:
            answer+=1
out = open("gymnastics.out", "w")
out.write(str(answer))
out.close()
file.close()
