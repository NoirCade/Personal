def solution(arr, queries):
    answer = []


    
    for i in queries:
        num = max(arr)
        chk = 0
        s = i[0]
        e = i[1]
        k = i[2]
        for j in arr[s:e+1]:
            if j > k:
                num = min(j, num)
                chk = 1
        
        if chk == 0:
            num = -1
        
        answer.append(num)
        
    return answer