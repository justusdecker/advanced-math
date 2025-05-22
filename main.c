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

int *MoveTo(int x1,
    int y1,
    int x2,
    int y2) {
    int *xy = GetDistance(x1,y1,x2,y2);
    int a = xy[0];
    int b = xy[1];
    //  angle alpha: sin^-1(a/sqrt(a^2+b^2)) 
    double alpha = asin(a / sqrt(pow(a,2) + pow(b,2)));

    double dx = sin(alpha);
    double dy = cos(alpha);
    
    // dx & dy must be positive for the next calculation
    if ( dx < 0 ) { dx *= -1; }
    if ( dy < 0 ) { dy *= -1; }

    // dx should be positive if a is above 0 vice versa
    // dy should be positive if a is above 0 vice versa
    if ( a >= 0 ) { dx *= -1; }
    if ( b >= 0 ) { dy *= -1; }

    // add this values to the start_position
    x1 += dx;
    y1 += dy;
    static int new_xy[2];
    new_xy[0] = (int) x1;
    new_xy[1] = (int) y1;
    return new_xy;
    }
    
int main() {
    int *xy = MoveTo(1,1,3,4);

    printf("the distance is %d %d", xy[0],xy[1]);
    return 0;
}
