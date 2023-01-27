line=input()
ints=list(map(int, line.split()))
ints.sort()
a=ints[0]
b=ints[1]
c=ints[6]-ints[1]-ints[0]
print(a, b, c)
