s=[]
t=[]
b=[]
for i in range(101):
    s.append(0)
    t.append(0)
    b.append(0)
file = open("blist.in", "r")
out = open("blist.out", "w")
n=int(file.readline())
for i in range(1,n+1):
    line=file.readline()
    line = list(line.split(" "))
    s[i],t[i],b[i]=line[0],line[1],line[2]
maxbuckets = 0
for time in range(1, 1001):
    buckets_at_this_time = 0
    for i in range(1,n+1):
        if (int(s[i]) <= time and time <= int(t[i])):
            buckets_at_this_time += int(b[i])
    maxbuckets = max(maxbuckets, buckets_at_this_time)
print(maxbuckets)
out.write(str(maxbuckets))
out.close()
file.close()
