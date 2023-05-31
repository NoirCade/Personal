import copy

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]

answer = []
temp = copy.deepcopy(arr)
idx1 = 0
idx2 = 0

for i in range(len(queries)):
    idx1 = queries[i][0]
    idx2 = queries[i][1]
    
    temp[idx1] = arr[idx2]
    temp[idx2] = arr[idx1]
    arr = copy.deepcopy(temp)
    
answer = arr
print(answer)
