# задача 1
X = [[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]
a = len(X)
b = len(X[0])
answer = 1for i in range(min(a, b)):
    if X[i][i] != 0:
        answer *= X[i][i]
print(answer)

# задача 2
x = [1, 2, 2, 4]
y = [4, 2, 1, 2]
x.sort()
y.sort()
if x == y:
    print(True)
else:
    print(False)

# задача 3

x = [6, 2, 0, 3, 0, 0, 5, 7, 0]
maxx = -100000
i = 0
while (i < len(x)):
    if x[i] == 0 and i != len(x)-1:
        i+=1
        maxx = max(maxx, x[i])
    else:
        i+=1   
print(maxx)

# задача 4


# задача 5

x = [2, 2, 2, 3, 3, 3, 5]
dict = {}
x1, x2 =[], []
for i in range(len(x)):
    if x[i] not in dict:
        dict[x[i]]=1
    else:
        dict[x[i]]+=1
for i in dict.keys():
    x1.append(i)
    x2.append(dict[i])
print((x1, x2))

# задача 6
