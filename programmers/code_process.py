def solution(code):
    answer = ''
    mode = 0
    ret = ''
    l = list(code)
    
    for i in range(len(l)):
        if l[i] == '1':
            mode = int(not mode)
        else:
            if (mode == 0) and ((i%2) == 0):
                ret += l[i]
                
            elif (mode == 1) and ((i%2) == 1):
                ret += l[i]
                
    if ret == '':
        answer = 'EMPTY'
    else:
        answer = ret
    return answer