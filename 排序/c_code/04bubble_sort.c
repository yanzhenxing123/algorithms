#include <stdio.h>
#include "malloc.h"

# define True 1
# define False 0

/*
 * 4. 冒泡排序
 */

void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void bubble_sort(int A[], int n) {
    for (int i = 0; i < n-1; ++i) { // 循环n-1次
        int flag = False;
        for (int j = n - 1; j > i; --j) { // 从后往前 将最小的元素放到第一个
            if (A[j - 1] > A[j]) {
                swap(&A[j - 1], &A[j]);
                flag = True;
            }
        }
        if (!flag) {
            return;
        }
    }
}

void out(int A[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[10] = {2, 3, 4, 6, 0, 10, 1, 2, 9, 5};
    int n = 10;
    bubble_sort(A, n);
    out(A, n);
}