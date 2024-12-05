file=open("cowsignal.in", 'r')
out = open("cowsignal.out", "w")
m,n,k = map(int, file.readline().split())
firstsignal=[]
for i in range(m):
    line=file.readline()
    line=line.rstrip()
    firstsignal.append(line)
newsignal=[]
for i in range(m):
    line=firstsignal[i]
    e=[]
    for a in range(n):
        for j in range(k):
            e.append(line[a])
    for b in range(k):
        newsignal.append(e)
for i in range(len(newsignal)):
    listToStr = ''.join([str(elem) for elem in newsignal[i]])
    listToStr=listToStr+'\n'
    out.write(listToStr)
file.close()
out.close()
