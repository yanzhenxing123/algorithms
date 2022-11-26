#include <stdio.h>

/*
 * 3. 希尔排序
 */

void shell_sort(int A[], int n) {
    int gap, i, j;
    for (gap = n / 2; gap >= 1; gap /= 2) { // gap循环
        for (i = gap + 1; i <= n; i++) { // i 循环
            if (A[i-gap] > A[i]){
                A[0] = A[i];
                for (j = i - gap; j > 0  && A[j] > A[0]; j -= gap) { // j 循环
                    A[j+gap] = A[j];
                }
                A[j+gap] = A[0];
            }
        }
    }
}

void out(int A[], int n) {
    for (int i = 1; i <= n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[11] = {10000, 2, 3, 4, 6, 0, 10, 1, 2, 9, 5};
    int n = 10;
    shell_sort(A, n);
    out(A, n);
}