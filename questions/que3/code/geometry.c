#include <math.h>

#define NUM 100

typedef struct {
    double x;
    double y;
} Vector2D;

extern void parabola_gen(double y[], double x[], double flen) {
    for (int i = 0; i < NUM; i++) {
        y[i] = -flen + i * (2 * flen / (NUM - 1));
        x[i] = (y[i] * y[i]) / (4 * 2);            
    }
}

extern void get_line(Vector2D* A, Vector2D* B) {
    A->x = 8;
    A->y = -8;
    B->x = 8;
    B->y = 8;
}

