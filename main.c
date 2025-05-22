#include <stdio.h>
#include <math.h>
int *GetDistance(int x1,
            int y1,
            int x2,
            int y2) {
    static int xy[2];
    xy[0] = x2 - x1;
    xy[1] = y2 - y1;
    
    return xy;
}
int main() {
    int *xy = GetDistance(1,1,3,4);

    printf("the distance is %d %d", xy[0],xy[1]);
    return 0;
}
