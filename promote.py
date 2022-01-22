file=open('promote.in','r')
out=open('promote.out','w')
bs,be = map(int, file.readline().split())
ss,se = map(int, file.readline().split())
gs,ge = map(int, file.readline().split())
ps,pe = map(int, file.readline().split())
gp=pe-ps
sp=ge-gs+gp
bp=se-ss+sp
print(bp,sp,gp)
bp,sp,gp=str(bp),str(sp),str(gp)
out.write(bp+'\n'+sp+'\n'+gp)
out.close()
file.close()
