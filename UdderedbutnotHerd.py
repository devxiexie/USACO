
'''n=int(input())
a=[]
b=[]
a=(list(map(int, input().split())))
b=(list(map(int, input().split())))
x=0
y=0
tot=0
factorial= 1
num=n
for i in range(1,num + 1):
       factorial = factorial*i
print(factorial)       
for i in range(111111111111111111111111111111111111111):
    if a[x] <= b[y]:
        tot=tot+1
        print(a[x],b[y],tot)
        y=y+1
    if y == n:
        y=0
        x=x+1
        continue
    if x == n and y == n:
        break
print(tot)'''

alphabet, hum = input(), input()
print(1 + sum([alphabet.find(hum[i+1]) <= alphabet.find(hum[i]) for i in range(len(hum)-1)]))
