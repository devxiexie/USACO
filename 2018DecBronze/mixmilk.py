file=open('mixmilk.in','r')
def pour(c1,m1,c2,m2):
    amount=min(m1,c2-m2)
    print(amount)
    m1-=amount
    m2+=amount
    return c1,m1,c2,m2
c1,m1 = map(int, file.readline().split())
c2,m2=map(int, file.readline().split())
c3,m3=map(int, file.readline().split())
for i in range(33):
    c1,m1,c2,m2=pour(c1, m1, c2, m2)
    c2, m2, c3, m3=pour(c2, m2, c3, m3)
    c3, m3, c1, m1=pour(c3, m3, c1, m1)
c1, m1, c2, m2=pour(c1, m1, c2, m2)
print(m1,m2,m3)
m1,m2,m3=str(m1),str(m2),str(m3)
o=open('mixmilk.out','w')
o.write(m1+'\n'+m2+'\n'+m3)
o.close()
file.close()
