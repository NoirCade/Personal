arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

for i in queries:
    s = i[0]
    e = i[1]
    k = i[2]
    for j in range(len(arr[s:e+1])):
        if (j%k == 0):
            arr[j] += 1

print(arr)