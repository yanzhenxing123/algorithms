#include <stdio.h>
#include "stdlib.h"

/*
 * 8. 归并排序
 */

int B[11]; // 辅助数组

void merge(int A[], int low, int mid, int high) {
    int i, j, p;
    for (p = low; p <= high; ++p) B[p] = A[p];

    for (p = low, i = low, j = mid + 1; i <= mid && j <= high; p++) {
        // 都是B中的比较, 不改变的
        if (B[i] < B[j]) A[p] = B[i++];
        else A[p] = B[j++];
    }

    while (i <= mid) A[p++] = B[i++];
    while (j <= high) A[p++] = B[j++];

}

void merge_sort(int A[], int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;
        merge_sort(A, low, mid);
        merge_sort(A, mid + 1, high);
        merge(A, low, mid, high);
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
    merge_sort(A, 1, 10);
    out(A, n);
}