#include <stdio.h>
#include "malloc.h"
#include "queue"
#include "stack"
#include "vector"

using namespace std;

/*
 * 10. ������ǰ�����
 *     1
 *   2   3       wpl = 4*3 + 5*3 + 3 = 21
 * 4   5
 *
 * ����ֵΪvoid�ĺ������׾� ���� if (!root) return;
 *
 * �з���ֵ�ĺ�����Ҫ���ǽڵ�Ϊ�շ���ʲô���ڵ㲻Ϊ�շ���ʲô
 *
 * ����Ҫ
 *      void func(root, path) {
 *          if (...) return;
 *          path.push_back(data)
 *          ...
 *          path.pop_back();
 *      }
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

// 1. �������
void pre_order(BTree root) {
    if (!root) return;
    visit(root);
    pre_order(root->lchild);
    pre_order(root->rchild);
}

// 1.2 �������
void pre_order2(BTree root) {
    if (!root) return;
    stack<BTree> S;
    BTree p = root;
    while (p || !S.empty()) {
        if (p) {
            visit(p);
            S.push(p);
            p = p->lchild;
        } else {
            p = S.top();
            S.pop();
            p = p->rchild;
        }
    }
}


// 2. �������
void in_order(BTree root) {
    if (!root) return;
    in_order(root->lchild);
    visit(root);
    in_order(root->rchild);
}

// 2.2 �������
void in_order2(BTree root) {
    if (!root) return;
    stack<BTree> S;
    BTree p = root;
    while (p || !S.empty()) {
        if (p) {
            S.push(p);
            p = p->lchild;
        } else {
            p = S.top();
            S.pop();
            visit(p);
            p = p->rchild;
        }
    }
}

// 3. �������
void post_order(BTree root) {
    if (!root) return;
    post_order(root->lchild);
    post_order(root->rchild);
    visit(root);
}

// 3.2 �������
void post_order2(BTree root) {
    if (!root) return;
    stack<BTree> s;
    BTree p = root, r = NULL; // r��¼��һ����һ�����ʵĽڵ�
    while (p || !s.empty()) {
        if (p) {
            s.push(p);
            p = p->lchild;
        } else {
            p = s.top(); // �Ȼ�ȡp�ڵ�
            if (p->rchild && p->rchild != r) {
                p = p->rchild;
            } else {
                s.pop();
                visit(p);
                r = p;
                p = NULL; // ����pָ��
            }
        }
    }
}

// 4. �������
void lever_order(BTree root) {
    if (!root) return;
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

// 5. �������е����ֵ
int max_value = -2147483648;

void max_by_pre_order(BTree root) {
    if (!root) return;

    if (root->data > max_value) max_value = root->data;
    max_by_pre_order(root->lchild);
    max_by_pre_order(root->rchild);
}

// 5.2 �������е����ֵ
int max_by_post_order(BTree root) {
    if (root == nullptr) return -1;
    int left = max_by_post_order(root->lchild);
    int right = max_by_post_order(root->rchild);
    return max(root->data, max(left, right)); // �Լ��ͺ��ӱȽ�
//    return max(root->data, max(max_by_post_order(root->lchild), max_by_post_order(root->rchild)));
}


// 6. �������߶� �������
int height(BTree root) {
    if (!root) return 0;
    int left = height(root->lchild);
    int right = height(root->rchild);
    return (left > right ? left : right) + 1;
}


// 7. wpl �������
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

// 8. ��·��
void search(BTree root, int x, vector<int> path) {
    // �������
    if (!root) return;

    path.push_back(root->data);
    if (root->data == x) {
        for (int i : path) {
            printf("%d\t", i);
        }
    }
    search(root->lchild, x, path);
    search(root->rchild, x, path);
    path.pop_back();
}

void out(int A[], int n) {
    for (int i = 1; i <= n; ++i) {
        printf("%d\t", A[i]);
    }
}

int main() {
    BTree root = create_tree();
    printf("�������:\n");
    pre_order(root);
    printf("\n�������2:\n");

    pre_order2(root);
    printf("\n�������:\n");
    in_order(root);
    printf("\n�������2:\n");
    in_order2(root);

    printf("\n�������:\n");
    post_order(root);

    printf("\n�������:\n");
    post_order2(root);
    printf("\n�������:\n");
    lever_order(root);
    printf("\n���ֵ:\n");
    max_by_post_order(root);
    printf("%d", max_by_post_order(root));
    printf("\n�߶�:\n");
    printf("%d", height(root));
    printf("\nwpl:\n");
    wpl(root, 0);
    printf("%d", wpl_value);
    printf("\n��·��:\n");
    vector<int> path;
    search(root, 4, path);

}