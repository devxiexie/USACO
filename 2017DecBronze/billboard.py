file = open("billboard.in", "r")
output = open("billboard.out", "w")
board1=(file.readline())
board2=(file.readline())
ad=(file.readline())
file.close()
def convert(string): 
    li = list(string.split(" ")) 
    return li

def area(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)

def visarea(x1,y1,x2,y2,x3,y3,x4,y4):
    Visiblearea=area(x1,x2,y1,y2)
    leftx=max(x1,x3)
    rightx=min(x2,x4)
    bottomy=max(y1,y3)
    topy=min(y2,y4)
    if(leftx < rightx and bottomy < topy):
        Visiblearea -= area(leftx, rightx, bottomy, topy)
    return Visiblearea
    
board1 = convert(board1)
board2 = convert(board2)
ad = convert(ad)

x1,y1,x2,y2=int(board1[0]),int(board1[1]),int(board1[2]),int(board1[3])
x3,y3,x4,y4=int(board2[0]),int(board2[1]),int(board2[2]),int(board2[3])
x5,y5,x6,y6=int(ad[0]),int(ad[1]),int(ad[2]),int(ad[3])

(tot) = visarea(x1, y1, x2, y2,x5,y5,x6,y6) + visarea(x3, y3, x4, y4,x5,y5,x6,y6)
output.write(str(tot))
output.close()
