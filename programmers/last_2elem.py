def solution(num_list):
    answer = []
    last = num_list[-1]
    before = num_list[-2]
    
    if last > before:
        num_list.append(last-before)
    else:
        num_list.append(2*last)
        
    answer = num_list
    return answer