def solution(a, b, c):
    answer = 0
    con1 = bool(a==b)
    con2 = bool(b==c)
    con3 = bool(c==a)
    if [con1, con2, con3] == [True, True, True]:
        answer = (a+b+c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3)
    elif [con1, con2, con3] == [False, False, False]:
        answer = (a+b+c)
    else:
        answer = (a+b+c)*(a**2 + b**2 + c**2)
    
    print(con1, con2, con3)
    return answer