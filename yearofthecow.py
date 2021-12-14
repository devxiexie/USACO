n=int(input())
years=["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]

arr=[]
for i in range(n):
	line = input().split(' ')
	arr.append([line[0], line[3], line[4], line[7]])

for i in range(n):
    
    if arr[i][3]=='Bessie':
        arr[i].append(years.index(arr[i][2]))
        arr[i].append(0)
    else:
        for j in range(i-1,-1,-1):
            if arr[j][0] == arr[i][3]:
                value = j
        arr[i].append(years.index(arr[i][2]))
        arr[i].append(years.index(arr[value][2]))
    if arr[i][1] == 'previous':
        if arr[i][4] >= arr[i][5]:
            arr[i].append(-12 + arr[i][4] - arr[i][5])
        else:
            arr[i].append(arr[i][4] - arr[i][5])
    else:
        if arr[i][4] <= arr[i][5]:
            arr[i].append(12 - (arr[i][5] - arr[i][4]))
        else:
            arr[i].append(arr[i][4] - arr[i][5])
    
    
    if arr[i][3] == 'Bessie':
        arr[i].append(arr[i][6])
    else:
        for j in range(i - 1, -1, -1):
            if arr[j][0] == arr[i][3]:
                value = j
                arr[i].append(arr[i][6] + arr[value][7])
    if arr[i][0] == 'Elsie':
        ans = arr[i][7]
        break

print(abs(ans))
