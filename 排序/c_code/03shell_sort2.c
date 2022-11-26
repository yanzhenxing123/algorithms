#include <stdio.h>

/*
 * 3.2 希尔排序
 * A[0]不是哨兵了, 并且是分趟排的，类比手算时的思路
 */

void shell_sort2(int A[], int n) {
    int gap, i, j;
    for (gap = n / 2; gap >= 1; gap /= 2) { // gap循环
        for (i = 0; i < gap; i++) { // gap次
            for (j = gap + i; j < n; j += gap) { //直接插入
                if (A[j - gap] > A[j]) {
                    int temp = A[j];
                    int k = j - gap;
                    while (k >= 0 && A[k] > temp) { // 找到最终位置
                        A[k + gap] = A[k];
                        k -= gap;
                    }
                    A[k + gap] = temp;
                }
            }
        }
    }
}

void out(int A[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[11] = {10000, 2, 3, 4, 6, 0, 10, 1, 2, 12};
    int n = 11;
    shell_sort2(A, n);
    out(A, n);
}