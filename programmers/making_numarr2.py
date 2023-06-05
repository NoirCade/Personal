import math
l = 5
r = 555

answer = []
l = list(range(l, r+1))

for i in l:
    if ((math.log(5, i)).is_integer()):
            print(l)