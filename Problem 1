file = open("herding.in", "r")
output = open("herding.out", "w")
n=file.readline()
n = list(n.split(" "))
file.close()

a,b,c=int(n[0]),int(n[1]),int(n[2])

if (a > b):
    a,b=b,a
if (b > c):
    b,c=c,b
if (a > b):
    a,b=b,a

if c==a+2:
    output.write('0\n')
elif b==a+2 or c==b+2:
    output.write('1\n')
else:
    output.write('2\n')
output.write(str(max(b-a, c-b)-1))
output.close()
