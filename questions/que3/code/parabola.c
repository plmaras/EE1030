#include <math.h>
#include <stdlib.h>

typedef struct {
  double **V;
  double *U;
  double f;
  int rows;
  int cols;
  int size;
} Parabola;

static double** createMat(int rows, int cols) {
  double **mat = (double **)malloc(rows * sizeof(double *));
  for (int i = 0; i < rows; i++) {
    mat[i] = (double *)malloc(cols * sizeof(double));
  }
  return mat;
}


static void freeMat(double **mat, int rows) {
  for (int i = 0; i < rows; i++) {
    free(mat[i]);
  }
  free(mat);
}

Parabola createParabola(int vRows, int vCols, int uSize, double f) {
  Parabola p;
  p.V = createMat(vRows, vCols);
  p.U = (double *)malloc(uSize * sizeof(double));
  p.f = f;
  p.rows = vRows;
  p.cols = vCols;
  p.size = uSize;
  return p;
}

double calculate_y(Parabola *p, double x) {

  double y = p->V[1][1] * x * x + p->V[1][0] * x + p->U[0] + p->f;
  return y;
}

void freeParabola(Parabola *p) {
  free(p->U);
  freeMat(p->V, p->rows);
}

