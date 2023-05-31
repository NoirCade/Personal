def solution(n, control):
    answer = 0
    l = list(control)
    ww = l.count('w')
    ss = l.count('s')
    dd = l.count('d')
    aa = l.count('a')
    
    answer = n + ww - ss + 10*dd - 10*aa
    
    return answer