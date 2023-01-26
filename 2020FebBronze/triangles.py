file = open("triangles.in", "r")
output = open("triangles.out", "w")
n=int(file.readline())
points=[]
listx=[]
listy=[]
total=[]
for q in range(n):
    points=(list(map(int, file.readline().split())))
    listx.append(points[0])
    listy.append(points[1])
file.close()

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if listx[i] == listx[j] and listy[i] == listy[k]:
                area = abs((listy[i]-listy[j])*(listx[i]-listx[k]))
                total.append(area) 
                print(area,i,j,k,total)
            elif listx[j] == listx[k] and listy[j] == listy[i]:
                area = abs((listy[j]-listy[k])*(listx[j]-listx[i]))
                total.append(area) 
                print(area,i,j,k,total)
            elif listx[k] == listx[i] and listy[k] == listy[j]:
                area = abs((listy[k]-listy[i])*(listx[k]-listx[j]))
                total.append(area) 
                print(area,i,j,k,total)

output.write("{}\n".format(int(max(total))))

output.close()
