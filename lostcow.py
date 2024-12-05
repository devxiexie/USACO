file = open("lostcow.in", "r")
output = open("lostcow.out", "w")
n=file.readline()
n = list(n.split(" "))
file.close()

x,y=int(n[0]),int(n[1])
by=1
direc=1
ans=0
while(True):
    if((direc==1 and x<=y and y<=x+by) or (direc==-1 and x-by<=y and y<=x)):
        ans += abs(y-x)
        output.write(str(ans))
        break
    else:
        ans += by*2
        by *= 2
        direc *= -1
output.close()
