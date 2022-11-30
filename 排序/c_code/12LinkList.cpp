#include <iostream>
#include "queue"
#include "stack"

typedef struct node {
    int data;
    struct node *next;
} LNode, *LinkList;

LinkList create() {
    LNode *head = NULL;
    LNode *p = head;
    for (int i = 0; i < 10; ++i) {
        LNode *node = (LNode *) malloc(sizeof(LNode));
        node->data = i;
        if (!p) {
            p = node;
            head = p;
        } else {
            p->next = node;
            p = p->next;
        }
    }
    p->next = nullptr;
    return head;
}


// 1. 反转(没有头节点)
LinkList reverse1(LinkList head) {
    LinkList new_head = nullptr;
    while (head) {
        // 头删
        LNode *node = head;
        head = head->next;

        // 头插
        node->next = new_head;
        new_head = node;
    }
    return new_head;
}

// 1.2 反转(有头节点)
void reverse2(LinkList head) {
    // 前后指针 0->1->2->3
    LNode *p = head->next, *q = p->next;
    head->next = nullptr;
    while (true) {
        // 头插
        p->next = head->next;
        head->next = p;
        // 头删
        p = q;
        if (!p) break; // 避免q空指针异常
        q = q->next;
    }
}

void out(LinkList head) {
    while (head != nullptr) {
        printf("%d\t", head->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    LinkList head = create();
    out(head);
    LinkList new_head = reverse1(head);
    out(new_head);
    reverse2(new_head);
    out(new_head);
}
