def solution(numLog):
    answer = ''
    chg = 0
    d = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    for i in range(len(numLog[:-1])):
        chg = numLog[i+1] - numLog[i]
        answer += d[chg]
    
    return answer