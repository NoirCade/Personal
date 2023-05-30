def solution(ineq, eq, n, m):
    answer = 0
    con1 = 0
    con2 = 0
    
    if ineq == '<':
        con1 = 0
    else:
        con1 = 1
        
    if eq == '=':
        con2 = 0
    else:
        con2 = 1
        
    if [con1, con2] == [0, 0]:
        answer = int(bool(n<=m))
    elif [con1, con2] == [0, 1]:
        answer = int(bool(n<m))
    elif [con1, con2] == [1, 0]:
        answer = int(bool(n>=m))
    elif [con1, con2] == [1, 1]:
        answer = int(bool(n>m))
        
    return answer