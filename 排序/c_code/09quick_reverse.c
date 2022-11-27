#include <stdio.h>
#include "malloc.h"

#define MaxSize 12500
/*
 * 三元组的快速转置
 */



typedef struct { // 元素单元
    int i, j; // 坐标
    int e;
} Triple;

typedef struct { // 三元组矩阵
    Triple data[MaxSize + 1];
    int mu, nu, tu; // 行数 列数 元素个数
} TSMatrix;

void quick_reverse(TSMatrix M, TSMatrix T) {
    // nums: 1 ~ n cpot: 1 ~ n
    int nums[M.nu + 1], cpot[M.nu + 1];
    cpot[1] = 1; // 初始化第一个
    T.mu = M.mu;
    T.nu = M.nu;
    T.tu = M.tu;

    for (int col = 1; col <= T.nu; ++col) {  // 初始化nums 1~nu
        nums[col] = 0;
    }

    for (int i = 1; i <= T.tu; ++i) { //
        ++nums[M.data[i].j]; // col = M.data[i].j ++nums[col]
    }

    for (int col = 2; col <= T.nu; ++col) { // cpot的 2 ~ nu
        cpot[col] = cpot[col - 1] + nums[col - 1];
    }

    for (int i = 1; i < T.nu; ++i) {
        int col = T.data[i].j;
        int q = cpot[col]; // T矩阵中的位置
        T.data[q].i = M.data[q].j;
        T.data[q].j = M.data[q].i;
        T.data[q].e = M.data[q].e;
        ++cpot[col];

    }

}

void out(int A[], int n) {
    for (int i = 1; i <= n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    int A[11] = {0, 5, 2, 3, 4, 6, 0, 10, 1, 2, 9};
    TSMatrix *T = (TSMatrix *) malloc(sizeof(TSMatrix));
    int n = 10;
    out(A, n);
}