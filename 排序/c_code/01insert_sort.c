#include <stdio.h>
#include "malloc.h"

/*
 * 1. 直插
 */

void insert_sort(int A[], int n) {
    for (int i = 2; i <= n; ++i) {
        int j;
        if (A[i - 1] > A[i]) {
            A[0] = A[i];
            for (j = i - 1; A[j] > A[0]; --j) {
                A[j + 1] = A[j];
            }
            A[j + 1] = A[0];
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
    insert_sort(A, n);
    out(A, n);
}