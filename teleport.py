file = open("teleport.in", "r")
output = open("teleport.out", "w")
line=file.readline()
file.close()

line=list(line.split(" "))

a,b,x,y=int(line[0]),int(line[1]),int(line[2]),int(line[3])


answer = abs(a-b)
answer = min(answer, abs(a-x) + abs(b-y))
answer = min(answer, abs(a-y) + abs(b-x))
output.write(str(answer))

output.close()