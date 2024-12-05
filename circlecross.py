file=open('circlecross.in','r')
line=file.readline()
cows=[]
print(line)
for l in line:
    cow=ord(l)-65
    cows.append(cow)
print(cows)
ans=0
for i in range(26):
    first = cows.index(i)
    reversed_list = cows[::-1]
    first_index_in_reversed = reversed_list.index(i)
    last = len(cows) -1 - first_index_in_reversed
    print(first,last)
    newlist=cows[first:last+1]
    print(newlist)

    for j in range(len(newlist)):
        if newlist.count(newlist[j])==1:
            ans+=1
            print('AAAA', newlist[j])
print(ans)
out=open('circlecross.out','w')
out.write(str(int(ans/2)))
out.close()
file.close()
