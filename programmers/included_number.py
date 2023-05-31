def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        number = a + d*i
        if included[i]:
            answer += number
            
    return answer