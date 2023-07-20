#include <stdio.h>
#include <stdlib.h>
#include "stdbool.h"

/*
// 13. 双端链表 复试考察，初试不考
*/
typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

typedef struct DoubleLinkedList {
    Node* head;
    Node* tail;
} DoubleLinkedList;

DoubleLinkedList* create_list() {
    DoubleLinkedList* list = (DoubleLinkedList*)malloc(sizeof(DoubleLinkedList));
    list->head = NULL;
    list->tail = NULL;
    return list;
}


void destroy_list(DoubleLinkedList* list) {
    Node* cur = list->head;
    while (cur != NULL) {
        Node* temp = cur;
        cur = cur->next;
        free(temp);
    }
    free(list);
}

void insert_front(DoubleLinkedList* list, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = list->head;
    if (list->head != NULL) {
        list->head->prev = new_node;
    } else {
        list->tail = new_node;
    }
    list->head = new_node;
}

void insert_back(DoubleLinkedList* list, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->prev = list->tail;
    new_node->next = NULL;
    if (list->tail != NULL) {
        list->tail->next = new_node;
    } else {
        list->head = new_node;
    }
    list->tail = new_node;
}


void insert_at(DoubleLinkedList* list, int index, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    if (index == 0) {
        new_node->prev = NULL;
        new_node->next = list->head;
        if (list->head != NULL) {
            list->head->prev = new_node;
        } else {
            list->tail = new_node;
        }
        list->head = new_node;
    } else {
        Node* cur = list->head;
        int i = 0;
        while (cur != NULL && i < index) {
            cur = cur->next;
            i++;
        }
        if (cur != NULL) {
            new_node->prev = cur->prev;
            new_node->next = cur;
            cur->prev->next = new_node;
            cur->prev = new_node;
        } else {
            new_node->prev = list->tail;
            new_node->next = NULL;
            if (list->tail != NULL) {
                list->tail->next = new_node;
            } else {
                list->head = new_node;
            }
            list->tail = new_node;
        }
    }
}

void remove_front(DoubleLinkedList* list) {
    if (list->head == NULL) {
        return;
    }
    Node* temp = list->head;
    list->head = list->head->next;
    if (list->head != NULL) {
        list->head->prev = NULL;
    } else {
        list->tail = NULL;
    }
    free(temp);
}

void remove_back(DoubleLinkedList* list) {
    if (list->tail == NULL) {
        return;
    }
    Node* temp = list->tail;
    list->tail = list->tail->prev;
    if (list->tail != NULL) {
        list->tail->next = NULL;
    } else {
        list->head = NULL;
    }
    free(temp);
}

void print_list(DoubleLinkedList* list) {
    Node* cur = list->head;
    while (cur != NULL) {
        printf("%d ", cur->data);
        cur = cur->next;
    }
    printf("\n");
}

int main() {
    DoubleLinkedList* list = create_list();
    insert_front(list, 3);
    insert_front(list, 2);
    insert_front(list, 1);
    insert_back(list, 4);
    insert_back(list, 5);
    insert_back(list, 6);
    print_list(list);
    remove_front(list);
    remove_back(list);
    print_list(list);
    destroy_list(list);
    return 0;
}
