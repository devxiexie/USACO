file=open('tttt.in','r')
tot=[]
l=file.readline()
l=l.rstrip('\n')
line1=[]
line1[:0]=l
tot.append(line1)
l=file.readline()
l=l.rstrip('\n')
line2=[]
line2[:0]=l
tot.append(line2)
l=file.readline()
l=l.rstrip('\n')
line3=[]
line3[:0]=l
tot.append(line3)
print(tot)
ans1,ans2=0,0
used1,used2=[],[]
for i in range(3):
    print(set(tot[i]))
    if len(set(tot[i]))==2 and set(tot[i]) not in used2:
        ans2+=1
        used2.append(set(tot[i]))
    if len(set(tot[i]))==1 and set(tot[i]) not in used1:
        ans1+=1
        used1.append(set(tot[i]))

for i in range(3):
    vert=[tot[0][i],tot[1][i],tot[2][i]]
    print('vert',vert)
    if len(set(vert))==2 and set(vert) not in used2:
        ans2+=1
        used2.append(set(vert))
    if len(set(vert))==1 and set(vert) not in used1:
        ans1+=1
        used1.append(set(vert))
        print('     ',i,used1,used2)

print(ans1,ans2)
diag1,diag2=[tot[0][0],tot[1][1],tot[2][2]],  [tot[0][2],tot[1][1],tot[2][0]]
print(diag1,diag2)
if len(set(diag1))==2 and set(diag1) not in used2:
    ans2+=1
    used2.append(set(diag1))
if len(set(diag1))==1 and set(diag1) not in used1:
    ans1+=1
    used1.append(set(diag1))
if len(set(diag2))==2 and set(diag2) not in used2:
    ans2+=1
    used2.append(set(diag2))
if len(set(diag2))==1 and set(diag2) not in used1:
    ans1+=1
    used1.append(set(diag2))
print(used1)
print(used2)
print(ans1,ans2)
o=open('tttt.out','w')
o.write(str(ans1)+'\n')
o.write(str(ans2))
o.close()
file.close()
