#include <stdio.h>
#include "malloc.h"

/*
 * 7.堆排序
 */

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heap_adjust(int A[], int k, int n) {
    A[0] = A[k];
    for (int i = 2 * k; i <= n; i *= 2) {
        if (i < n && A[i] < A[i + 1]) i++;
        if (A[0] > A[i]) break;
        else {
            A[k] = A[i];
            k = i;
        }
    }
    A[k] = A[0];
}

void build_max_heap(int A[], int n) {
    // 从后往前 n/2 ~ 1
    for (int i = n / 2; i >= 1; --i) {
        heap_adjust(A, i, n);
    }
}

void heap_sort(int A[], int n) {
    // 创建堆
    build_max_heap(A, n);
    // 调整n-1次根为1的堆 从 n~2
    for (int i = n; i > 1; i--) {
        swap(&A[i], &A[1]);
        heap_adjust(A, 1, i - 1); // ★
    }
}

void out(int A[], int n) {
    for (int i = 1; i <= n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[11] = {0, 5, 2, 3, 4, 6, 0, 10, 1, 2, 9};
    int n = 10;
    heap_sort(A, n);
    out(A, n);
}