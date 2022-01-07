import itertools

file=open('lineup.in', 'r')
out=open('lineup.out', 'w')
cows=['Beatrice', 'Belinda', 'Bella','Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
n=int(file.readline())
def perms(lst):
    perms = sorted(list(itertools.permutations(lst)))
    return perms
newcows=perms(cows)
ba,bb=[],[]
def where(c,j):
    for i in range(8):
        if newcows[j][i]==c:
            return i
''''
def satisfiy():
    for i in range(n):
        if (abs(where(ba[i])-where(bb[i]))!=1):
            return False
    return True
'''


for i in range(n):
    a,nothing1,nothing2,nothing3,nothing,b=map(str, file.readline().split())
    ba.append(a)
    bb.append(b)
print(ba,bb)
for i in range(len(newcows)):
    satisfiy=True
    for j in range(n):
        if(abs(where(ba[j],i)- where(bb[j],i)) != 1):
            satisfiy=False
        if satisfiy==False:
            break
    if(satisfiy):
        for x in range(8):
            print(newcows[i][x])
            out.write(newcows[i][x]+'\n')
        break
file.close()
out.close()
