#include <stdio.h>
#include "malloc.h"

/*
 * 6.选择排序
 */
void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void select_sort(int A[], int n) {
    for (int i = 0; i < n - 1; ++i) { // n-1次 0 ~ n-2
        int min = i;
        for (int j = i + 1; j < n; ++j) { // i+1 ~ n-1
            if (A[min] > A[j]) {
                min = j;
            }
        }
        if (min != i) {
            swap(&A[min], &A[i]);
        }
    }
}

void out(int A[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[10] = {5, 2, 3, 4, 6, 0, 10, 1, 2, 9};
    int n = 10;
    select_sort(A, n);
    out(A, n);
}