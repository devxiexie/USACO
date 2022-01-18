def commonelems(a, b):
    return bool(set(a) & set(b))
file=open('cownomics.in', 'r')
n,m = map(int, file.readline().split())
spotty,plain=[],[]
for i in range(n):
    line=file.readline()
    spotty.append(line)
for i in range(n):
    line=file.readline()
    plain.append(line)
ans=0
for i in range(m):
    charspot=[]
    charplain=[]
    for j in range(n):
        charspot.append(spotty[j][i])
    for j in range(n):
        charplain.append(plain[j][i])
    print(charspot,charplain,commonelems(charspot,charplain))
    #ans+=commonelems(charspot,charplain)
    if commonelems(charspot,charplain) is False:
        ans+=1
print(ans)
out = open("cownomics.out", "w")
out.write(str(ans))
out.close()
file.close()
