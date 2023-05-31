def solution(num_list):
    answer = 0
    ev = ''
    od = ''
    
    for i in num_list:
        if (i%2) == 0:
            ev += str(i)
        else:
            od += str(i)
            
    answer = int(ev) + int(od)
        
    return answer