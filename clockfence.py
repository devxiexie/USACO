n=int(input())
lst=[]
for i in range(0, n):
    ele=input()
    lst.append(ele)
def anglefd(a):
    if(a == 'E'): 
        return 0
    if(a == 'N'):
        return 90
    if(a == 'W'):
        return 180
    if(a == 'S'):
        return 270
def change(a,b):
    t1 = anglefd(a)
    t2 = anglefd(b)
    if(t2 == (t1 + 90)%360):
        return 90
    elif(t2 == t1):
        return 0
    elif(t2 == (t1 + 270)%360): 
        return -90
for i in range(n):
    s=lst[i]
    totalchange=0
    for i in range(len(s)):
        totalchange += change(s[i],s[(i+1)%len(s)])
    if(totalchange == 360):
        print("CCW")
    else:
        print("CW")
