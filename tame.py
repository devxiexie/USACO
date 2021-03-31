
file = open("taming.in", "r")
output = open("taming.out", "w")
n=int(file.readline())
breakdays=file.readline()
file.close()
breakdays = list(breakdays.split(" "))
if int(breakdays[0]) > 0:
    output.write('-1')

breakdays[0]='0'
t=-1
req=0
pos=0
j=n
for i in range(0,n):

    j-=1
    #if t != -1 and breakdays[j] != -1 and breakdays[j] #!= t:
        #output.write('-1')
    if(t == -1):
	    t = int(breakdays[j])
	
    if(int(breakdays[j]) == -1):
	    breakdays[i] = t
	
    if(int(breakdays[j]) == 0):
	    req+=1
	
    if(int(breakdays[j]) == -1):
	    pos+=1
	
    if(t > -1):
	    t-=1
ans=str(req)+' '+str(req+pos)

output.write(ans)
output.close()