n=int(input())
A=[]
for i in range(1001):
    b=[]
    for j in range(1001):
        b.append(0)
    A.append(b)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def validposition(x, y):
    if(x>=0 and x<=n and y>=0 and y<=n):
        return True
    else:
        return False
def comfortable(x,y):
    if A[x][y]==0:
        return 0
    neighbors=0
    for d in range(4):
        if(validposition(x+dx[d], y+dy[d])):
            if(A[x+dx[d]][y+dy[d]]==1):
                neighbors+=1
    if(neighbors==3):
        return 1
    else:
        return 0

comfnum=0
for i in range(int(n)):
    x,y =(map(int, input().split()))
    
    for d in range(4):
        if(validposition(x+dx[d],y+dy[d])):
            comfnum -= comfortable(x+dx[d],y+dy[d])
            
    A[x][y]=1
    
    for d in range(4):
        if(validposition(x+dx[d],y+dy[d])):
            comfnum += comfortable(x+dx[d],y+dy[d])
            #print(comfnum, x+dx[d],y+dy[d])
            
    comfnum+=comfortable(x,y)
    print(comfnum)
