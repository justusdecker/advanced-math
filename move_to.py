from math import sin, cos,asin,sqrt
def move_to(x1,y1,x2,y2):
    a = x2 - x1
    b = y2 - y1
    """
    Some strange bug occures here:
    in case a is positive and b negative the player will never find the goal
    what is the problem here?
    the values dx & dy will forever change between 2 values that are the same
    
    """
    alpha = asin(a / sqrt(a ** 2 + b ** 2))
    dx = abs(sin(alpha)) * (1 if a >= 0 else -1)
    dy = abs(cos(alpha)) * (1 if b >= 0 else -1)
    
    x1 += dx
    y1 += dy
    
    return [x1,y1]
def same_pos(p1,p2):
    return get_as_int(p1) == get_as_int(p2)
def get_as_int(p):
    return [int(i) for i in p]
pos1 = [1,3]
pos2 = [6,7]
while not same_pos(pos1,pos2):
    print('------------------------')
    for y in range(10):
        for x in range(15):
            if [x,y] == get_as_int(pos1) or [x,y] == get_as_int(pos2):
                print('#',end='')
            else:
                print(' ',end='')
        print()
    pos1 = move_to(*pos1,*pos2)
    print(pos1)
print('finished')
