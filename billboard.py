file = open("billboard.in", "r")
output = open("billboard.out", "w")
ad=(file.readline())
board=(file.readline())
file.close()
def convert(string): 
    li = list(string.split(" ")) 
    return li

def area(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)

    
board = convert(board)
ad = convert(ad)

x3,y3,x4,y4=int(board[0]),int(board[1]),int(board[2]),int(board[3])
x1,y1,x2,y2=int(ad[0]),int(ad[1]),int(ad[2]),int(ad[3])

def covered(x,y,x1,y1,x2,y2):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2;

corners=0

if covered(x1, y1, x3, y3, x4, y4):
    corners+=1
if covered(x1, y2, x3, y3, x4, y4):
    corners+=1
if covered(x2, y1, x3, y3, x4, y4):
    corners+=1
if covered(x2, y2, x3, y3, x4, y4):
    corners+=1

if corners==1 or corners==0:
    output.write(str((x2-x1)*(y2-y1)))
if corners==4:
    output.write('0')
if corners==2:
    xl=max(x1,x3)
    xr=min(x2,x4)
    yl=max(y1,y3)
    yr=min(y2,y4)
    print(xl,yl,xr,yr)
    output.write(str(((x2-x1)*(y2-y1))-(xr-xl)*(yr-yl)))
output.close()
