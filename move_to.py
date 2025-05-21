from math import sin, cos,asin,sqrt
from random import randint as ri
from time import perf_counter as pc
def move_to(x1:float,
            y1:float,
            x2:float,
            y2:float) -> list[float, float]:
    a = x2 - x1 # get x delta
    b = y2 - y1 # get y delta

    alpha = asin(a / sqrt(a ** 2 + b ** 2)) # a / sqrt(a**2+b**2)
    dx = abs(sin(alpha)) * (1 if a >= 0 else -1) # dx should be positive if a is above 0 vice versa
    dy = abs(cos(alpha)) * (1 if b >= 0 else -1) # dy should be positive if b is above 0 vice versa

    x1 += dx # add this values to the start_position
    y1 += dy # add this values to the start_position
    
    return [x1,y1]
def same_pos(
    p1: list[float,float],
    p2: list[float,float]) -> bool:
    return floor_ceil(*p1) == floor_ceil(*p2)
def get_as_int(p:list[float,float]) -> list[int,int]:
    return [int(i) for i in p]
def floor_ceil(x:float,y:float) -> list[int,int]:
    _x,_y = x - int(x) >= .5,y - int(y) >= .5
    return [int(x) + 1 if x - int(x) >= .5 else int(x),int(y) + 1 if y - int(y) >= .5 else int(y)]

pos1 = [6,7]
pos2 = [1,9]
MAX = 1024
TESTS = 8192
unit_tests = (([ri(0,128) for i in range(2)],[ri(0,MAX) for i in range(2)]) for c in range(TESTS))

comp = pc()
for nr,ut in enumerate(unit_tests):
    t = pc()
    
    pos1, pos2 = ut
    f = pos1.copy()
    while not same_pos(pos1,pos2):
        """print('------------------------')
        for y in range(10):
            for x in range(15):
                if [x,y] == get_as_int(pos1) or [x,y] == get_as_int(pos2):
                    print('#',end='')
                else:
                    print(' ',end='')
            print()"""
        pos1 = move_to(*pos1,*pos2)
        #print(pos1)
    print(f'finished unit_test Nr.{nr} [{f}] to [{pos2}] in {(pc()-t)*1000:.2f} ms')
print('------------------')
print(f'finished all tests in {(pc()-comp)*1000:.2f} ms')
