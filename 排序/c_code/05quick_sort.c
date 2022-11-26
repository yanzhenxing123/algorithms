#include <stdio.h>
#include "malloc.h"

/*
 * 5. 快速排序
 */

int partition(int A[], int low, int high) {
    int pivot = A[low];
    while (low < high) { // 最终位置为low = high
        while (low < high && A[high] >= pivot) high--;
        A[low] = A[high];
        while (low < high && A[low] <= pivot) low++;
        A[high] = A[low];
    }
    A[low] = pivot;
    return low;
}

void quick_sort(int A[], int low, int high) {
    if (low < high) {
        int pivotPos = partition(A, low, high);
        quick_sort(A, low, pivotPos - 1);
        quick_sort(A, pivotPos + 1, high);
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
    int low = 0, high = n-1;
    quick_sort(A, low, high);
    out(A, n);
}