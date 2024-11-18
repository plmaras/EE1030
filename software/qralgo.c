#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

#define MAX_ITER 3000
#define TOLERANCE 1e-15

typedef struct {
    double real;
    double imag;
} Complex;


Complex make_complex(double real, double imag) {
    Complex c = {real, imag};
    return c;
}


double complex_abs(Complex c) {
    return sqrt(c.real * c.real + c.imag * c.imag);
}


void householdertransform(double **A, int n, int k, double *v, double **H) {
    double alpha = 0.0;
    for (int i = k; i < n; i++) {
        alpha += A[i][k] * A[i][k];
    }
    alpha = sqrt(alpha);

    if (alpha > 0) {
        if (A[k][k] > 0) alpha = -alpha;

        double r = sqrt(0.5 * (alpha * alpha - A[k][k] * alpha));

        v[k] = (A[k][k] - alpha) / (2.0 * r);

        for (int i = k + 1; i < n; i++) {
            v[i] = A[i][k] / (2.0 * r);
        }

        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                H[i][j] = (i == j) ? 1 : 0;
            }
        }

        for (int i = k; i < n; i++) {
            for (int j = k; j < n; j++) {
                H[i][j] -= 2 * v[i] * v[j];
            }
        }

        
        double **A_temp = malloc(n * sizeof(double *));
        for (int i = 0; i < n; i++) {
            A_temp[i] = malloc(n * sizeof(double));
            for (int j = 0; j < n; j++) {
                A_temp[i][j] = 0;
                for (int l = 0; l < n; l++) {
                    A_temp[i][j] += H[i][l] * A[l][j];
                }
            }
        }

        // Copy A_temp to A
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = A_temp[i][j];
            }
        }

        for (int i = 0; i < n; i++) {
            free(A_temp[i]);
        }
        free(A_temp);
    }
}


void qr_decomposition(double **A, int n, double **Q, double **R) {
    double *v = malloc(n * sizeof(double));
    double **H = malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        H[i] = malloc(n * sizeof(double));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i][j] = (i == j) ? 1 : 0;
        }
    }

    for (int k = 0; k < n - 1; k++) {
        householdertransform(A, n, k, v, H);

     
        double **Q_temp = malloc(n * sizeof(double *));
        for (int i = 0; i < n; i++) {
            Q_temp[i] = malloc(n * sizeof(double));
            for (int j = 0; j < n; j++) {
                Q_temp[i][j] = 0;
                for (int l = 0; l < n; l++) {
                    Q_temp[i][j] += Q[i][l] * H[l][j];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Q[i][j] = Q_temp[i][j];
            }
        }

        for (int i = 0; i < n; i++) {
            free(Q_temp[i]);
        }
        free(Q_temp);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            R[i][j] = (i <= j) ? A[i][j] : 0;
        }
    }

    free(v);
    for (int i = 0; i < n; i++) {
        free(H[i]);
    }
    free(H);
}

void findeigenvalues(double a11, double a12, double a21, double a22, Complex *eig1, Complex *eig2) {
    double trace = a11 + a22;
    double det = a11 * a22 - a12 * a21;
    double discriminant = trace * trace - 4 * det;

    if (discriminant >= 0) {
        double sqrt_disc = sqrt(discriminant);
        eig1->real = (trace + sqrt_disc) / 2;
        eig1->imag = 0;
        eig2->real = (trace - sqrt_disc) / 2;
        eig2->imag = 0;
    } else {
        
        eig1->real = trace / 2;
        eig1->imag = sqrt(-discriminant) / 2;
        eig2->real = trace / 2;
        eig2->imag = -sqrt(-discriminant) / 2;
    }
}


void qr_algorithm(double **A, int n, Complex *eigenvalues) {
    double **Q = malloc(n * sizeof(double *));
    double **R = malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        Q[i] = malloc(n * sizeof(double));
        R[i] = malloc(n * sizeof(double));
    }

    for (int iter = 0; iter < MAX_ITER; iter++) {
        qr_decomposition(A, n, Q, R);

   
        double **A_temp = malloc(n * sizeof(double *));
        for (int i = 0; i < n; i++) {
            A_temp[i] = malloc(n * sizeof(double));
            for (int j = 0; j < n; j++) {
                A_temp[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    A_temp[i][j] += R[i][k] * Q[k][j];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = A_temp[i][j];
            }
        }

        for (int i = 0; i < n; i++) {
            free(A_temp[i]);
        }
        free(A_temp);

        
        int i = 0;
        while (i < n) {
            if (i == n - 1) {
                
                eigenvalues[i] = make_complex(A[i][i], 0);
                i++;
            } else if (fabs(A[i+1][i]) < TOLERANCE) {
                eigenvalues[i] = make_complex(A[i][i], 0);
                i++;
            } else {
                
                Complex eig1, eig2;
                findeigenvalues(A[i][i], A[i][i+1], A[i+1][i], A[i+1][i+1], &eig1, &eig2);
                eigenvalues[i] = eig1;
                eigenvalues[i+1] = eig2;
                i += 2;
            }
        }

        
        int converged = 1;
        for (int i = 0; i < n - 1; i++) {
            if (fabs(A[i+1][i]) > TOLERANCE) {
                converged = 0;
                break;
            }
        }
        if (converged) break;
    }

   
    for (int i = 0; i < n; i++) {
        free(Q[i]);
        free(R[i]);
    }
    free(Q);
    free(R);
}

int main() {
    int n;
    printf("Enter the size of the matrix: ");
    scanf("%d", &n);

    
    double **A = malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        A[i] = malloc(n * sizeof(double));
    }

    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    Complex *eigenvalues = malloc(n * sizeof(Complex));

    
    qr_algorithm(A, n, eigenvalues);

    
    printf("\nEigenvalues:\n");
    for (int i = 0; i < n; i++) {
        if (fabs(eigenvalues[i].imag) < TOLERANCE) {
            printf("%.6f\n", eigenvalues[i].real);
        } else {
            printf("%.6f %c %.6fi\n", 
                   eigenvalues[i].real,
                   eigenvalues[i].imag >= 0 ? '+' : '-',
                   fabs(eigenvalues[i].imag));
        }
    }


    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);
    free(eigenvalues);

    return 0;
}