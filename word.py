file=open('word.in', 'r')
out = open("word.out", "w")
n,k = map(int, file.readline().split())
words=[str(x) for x in file.readline().split()]
print(words)
line=[]
for i in range(n):
    line.append(words[i])
    can=(len(''.join(map(str, line)))<=k)
    line.pop()
    if can:
        line.append(words[i])
        
    if not can:
        line=' '.join(line)
        print(line)
        out.write(line+'\n')
        line=[]
        line.append(words[i])
line=' '.join(line)
print(line)
out.write(line)
out.close()
file.close()
