file=open('blocks.in','r')
n=int(file.readline())
one,two=[],[]
letters=[0]*26
for i in range(n):
    first,second = map(str, file.readline().split())
    one.append(first)
    two.append(second)
for i in range(n):
    firstused,secondused,first,second=[0]*26,[0]*26,[],[]
    first[:0],second[:0]=one[i],two[i]
    print(first,second)
    for j in range(len(first)):
        num=ord(first[j])-97
        print('f',ord(first[j]),num,first[j])
        firstused[num]+=1
    for j in range(len(second)):
        num=ord(second[j])-97
        print('f',ord(second[j]),num,second[j])
        secondused[num]+=1
    for j in range(26):
        x=max(firstused[j],secondused[j])
        letters[j]+=x
print(letters)
o=open('blocks.out','w')
for i in range(26):
    o.write(str(letters[i])+'\n')
o.close()
