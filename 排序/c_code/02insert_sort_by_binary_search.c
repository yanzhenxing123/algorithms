#include <stdio.h>
#include "malloc.h"

/*
 * 2. 二分查找直插
 */

void insert_sort_by_binary_search(int A[], int n) {
    int i, j, low, high, mid;
    for (i = 2; i <= n; ++i) {
        if (A[i - 1] > A[i]) {
            A[0] = A[i];
            low = 1, high = i - 1;
            // 找到最终位置 high+1
            while (low <= high) {
                mid = (low + high) / 2;
                if (A[0] < A[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            // 数据移动
            for (j = i - 1; j >= high + 1; --j) {
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
    insert_sort_by_binary_search(A, n);
    out(A, n);
}