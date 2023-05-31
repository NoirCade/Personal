def solution(num_list):
    answer = 0
    muls = 1
    sums = 0
    for i in num_list:
        muls *= i
        sums += i
        
    if muls < (sums**2):
        answer = 1
    
    return answer