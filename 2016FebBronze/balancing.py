file=open('balancing.in', 'r')
n,b = map(int, file.readline().split())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int, file.readline().split())
print(x,y)

ans=n
for xindex in range(n):
    for yindex in range(n):
        xfen=x[xindex]+1
        yfen=y[yindex]+1
        ul,ur,ll,lr=0,0,0,0
        for i in range(n):
            if(x[i]<xfen and y[i]<yfen):
                ll+=1
            if(x[i]<xfen and y[i]>yfen):
                ul+=1
            if(x[i]>xfen and y[i]<yfen):
                lr+=1
            if(x[i]>xfen and y[i]>yfen):
                ur+=1
        worst=0
        if ul>worst:
            worst=ul
        if ur>worst:
            worst=ur
        if ll>worst:
            worst=ll
        if lr>worst:
            worst=lr
        if worst<ans:
            ans=worst
print(ans)
out = open("balancing.out", "w")
out.write(str(ans))
out.close()
file.close()
