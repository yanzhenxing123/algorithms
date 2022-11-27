#include <stdio.h>
#include "malloc.h"
#include "queue"

using namespace std;

/*
 * 10. 二叉树前序遍历
 *     1
 *   2   3       wpl = 4*3 + 5*3 + 3 = 21
 * 4   5
 */

typedef struct BiTNode {
    int data;
    struct BiTNode *lchild, *rchild;
} BNode, *BTree;

BTree create_node(int data) {
    BTree root = (BNode *) malloc(sizeof(BNode));
    root->data = data;
    root->lchild = NULL;
    root->rchild = NULL;
    return root;
}

BTree create_tree() {
    BNode *root = create_node(1);
    BNode *node2 = create_node(2);
    BNode *node3 = create_node(3);
    BNode *node4 = create_node(4);
    BNode *node5 = create_node(5);

    root->lchild = node2;
    root->rchild = node3;
    node2->lchild = node4;
    node2->rchild = node5;
    return root;
}

void visit(BNode *node) {
    printf("%d\t", node->data);
}

// 1. 先序遍历
void pre_order(BTree root) {
    if (root) {
        visit(root);
        pre_order(root->lchild);
        pre_order(root->rchild);
    }
}


// 2. 中序遍历
void in_order(BTree root) {
    if (root) {
        in_order(root->lchild);
        visit(root);
        in_order(root->rchild);
    }
}

// 3. 后序遍历
void post_order(BTree root) {
    if (root) {
        post_order(root->lchild);
        post_order(root->rchild);
        visit(root);
    }
}

// 4. 层序遍历
void lever_order(BTree root) {
    if (root) {
        queue<BNode *> Q;
        Q.push(root);
        while (!Q.empty()) {
            BNode *node = Q.front();
            Q.pop();
            visit(node);
            if (node->lchild) {
                Q.push(node->lchild);
            }
            if (node->rchild) {
                Q.push(node->rchild);
            }
        }
    }
}

// 5. 二叉树中的最大值
int max_value = -2147483648;

void max_by_pre_order(BTree root) {
    if (root) {
        if (root->data > max_value) max_value = root->data;
        max_by_pre_order(root->lchild);
        max_by_pre_order(root->rchild);
    }
}

// 5.2 二叉树中的最大值
int max_by_post_order(BTree root) {
    if (root == nullptr) return -1;
    int left = max_by_post_order(root->lchild);
    int right = max_by_post_order(root->rchild);
    return max(root->data, max(left, right)); // 自己和孩子比较
//    return max(root->data, max(max_by_post_order(root->lchild), max_by_post_order(root->rchild)));
}


// 6. 二叉树高度 后序遍历
int height(BTree root) {
    if (!root) return 0;
    int left = height(root->lchild);
    int right = height(root->rchild);
    return (left > right ? left : right) + 1;
}


// 7. wpl 先序遍历
int wpl_value = 0;

void wpl(BTree root, int height) {
    if (root) {
        if (!root->lchild && !root->rchild) {
            wpl_value += root->data * height;
        }
        wpl(root->lchild, height + 1);
        wpl(root->rchild, height + 1);
    }
}

void out(int A[], int n) {
    for (int i = 1; i <= n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    BTree root = create_tree();
    printf("先序遍历:\n");
    pre_order(root);
    printf("\n中序遍历:\n");
    in_order(root);
    printf("\n后序遍历:\n");
    post_order(root);
    printf("\n层序遍历:\n");
    lever_order(root);
    printf("\n最大值:\n");
    max_by_post_order(root);
    printf("%d", max_by_post_order(root));
    printf("\n高度:\n");
    printf("%d", height(root));
    printf("\nwpl:\n");
    wpl(root, 0);
    printf("%d", wpl_value);


}