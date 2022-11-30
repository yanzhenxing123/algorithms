#include <iostream>
#include "queue"
#include "stack"

#define n 5
using namespace std;

/*
 * 11. 图相关算法
 *
 * a——b——c
 * | \
 * d——e
 *
 * a——>b——>c
 * | \
 * d——e
 *
 * 0 1 0 1 1
 * 1 0 1 0 0
 * 0 1 0 0 0
 * 1 0 0 0 1
 * 1 0 0 1 0
 *
 *
 */

// 无向图 最一般的
int a1[5][5] = {
        {0, 1, 0, 1, 1},
        {1, 0, 1, 0, 0},
        {0, 1, 0, 0, 0},
        {1, 0, 0, 0, 1},
        {1, 0, 0, 1, 0}
};
// 无向图 有权值的
int a2[5][5] = {
        {INT_MAX, 1, INT_MAX, 3,       4},
        {1, INT_MAX, 2,       INT_MAX, INT_MAX},
        {INT_MAX, 2, INT_MAX, INT_MAX, INT_MAX},
        {3, INT_MAX, INT_MAX, INT_MAX, 5},
        {4, INT_MAX, INT_MAX, 5,       INT_MAX}
};

// 有向图,拓扑排序
int a3[5][5] = {
        {0, 1, 1, 1, 1},
        {0, 0, 1, 1, 1},
        {0, 0, 0, 1, 1},
        {0, 0, 0, 0, 1},
        {0, 0, 0, 0, 0}
};


// 边节点
typedef struct ArcNode {
    int adjvex;
    struct ArcNode *nextArc;
} ArcNode;

// 顶点
typedef struct VNode {
    char data;
    ArcNode *firstArc;
} VNode;

// 邻接表
typedef struct ALGraph {
    int vex_num, arc_num;
    VNode adjList[n];
} ALGraph;

// 邻接矩阵单元
typedef struct {
    char vertex[n];
    int arcs[n][n];
    int vex_num, arc_num;
} MGraph;

MGraph createMGraph(int a[n][n]) {
    MGraph MG;
    MG.arc_num = 5;
    MG.vex_num = 5;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            MG.arcs[i][j] = a[i][j];
        }
    }
    MG.vertex[0] = 'a';
    MG.vertex[1] = 'b';
    MG.vertex[2] = 'c';
    MG.vertex[3] = 'd';
    MG.vertex[4] = 'e';

    return MG;
}

// 1. 邻接表转临界矩阵
MGraph ALGraph2MGraph(ALGraph AG, MGraph MG) {
    MG.arc_num = AG.arc_num;
    MG.vex_num = AG.vex_num;
    ArcNode *p;
    for (int i = 0; i < AG.vex_num; ++i) {
        for (p = AG.adjList[i].firstArc; p != nullptr; p = p->nextArc) {
            MG.arcs[i][p->adjvex] = 1;
        }
    }

    for (int i = 0; i < AG.vex_num; ++i) {
        MG.vertex[i] = AG.adjList[i].data;
    }
    return MG;
}

// 2. 邻接矩阵转临界表
ALGraph MGraph2ALGraph(MGraph MG, ALGraph AG) {
    AG.arc_num = MG.arc_num;
    AG.vex_num = MG.vex_num;

    // 先拷贝数据
    for (int i = 0; i < MG.vex_num; ++i) {
        AG.adjList[i].data = MG.vertex[i];
        AG.adjList[i].firstArc = nullptr;
    }

    // 然后拷贝关系
    for (int i = 0; i < MG.vex_num; ++i) {
        for (int j = 0; j < MG.vex_num; ++j) {
            // 头插
            if (MG.arcs[i][j]) {
                ArcNode *p = (ArcNode *) malloc(sizeof(ArcNode));
                p->adjvex = j;
                p->nextArc = AG.adjList[i].firstArc;
                AG.adjList[i].firstArc = p;
            }
        }

    }

    return AG;
}

void visit(ALGraph G, int v) {
    printf("%c\t", G.adjList[v].data);
}

int visited[n] = {0, 0, 0, 0, 0};

void init_visited() {
    for (int &i : visited) {
        i = 0;
    }
}

// 3. DFS
void DFS(ALGraph G, int v) {
    visited[v] = 1;
    visit(G, v);
    for (ArcNode *p = G.adjList[v].firstArc; p != nullptr; p = p->nextArc) {
        if (!visited[p->adjvex]) {
            DFS(G, p->adjvex);
        }
    }
}


// 4. BFS
void BFS(ALGraph G, int v) {
    // 一个连通分量的bfs
    queue<int> Q;
    visited[v] = 1;
    visit(G, v);
    Q.push(v);
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        for (ArcNode *w = G.adjList[u].firstArc; w != nullptr; w = w->nextArc) {
            if (!visited[w->adjvex]) {
                visit(G, w->adjvex);
                visited[w->adjvex] = 1;
                Q.push(w->adjvex);
            }

        }
//        邻接矩阵
//        for (int j = 0; j < G.vex_num; j++){
//            if (G.arcs[v][j] == 1 && !visited[j]){
//                cout << "->";
//                cout << G.vertex[j];//访问结点
//                visited[j] = true;
//                Q.push(j);//入队
//            }
//        }
    }

}

void BFSTraverse(ALGraph G) {
    init_visited();
    for (int i = 0; i < G.vex_num; i++) {//对每个连通分量进行遍历
        if (!visited[i]) BFS(G, i);
    }
//    init_visited();
//    for (int i = 4; i >= 0; i--) {//对每个连通分量进行遍历
//        if (!visited[i]) BFS(G, i);
//    }
}

// 5. 无向图找一个简单路径
void find_path(ALGraph G, int start, int end, vector<int> path) {
    path.push_back(start);
    // 终止条件 start == end
    if (start == end) for (int i : path) printf("%d\t", i);
    visited[start] = 1;
    // dfs
    for (ArcNode *p = G.adjList[start].firstArc; p != nullptr; p = p->nextArc) {
        if (!visited[p->adjvex]) {
            find_path(G, p->adjvex, end, path);
        }
    }
    path.pop_back();
}

// 6.prim算法
typedef struct {
    int adjvex;
    int lowcost;
} Closedge;


int minimum(Closedge closedge[]) {
    /*
     * 获取closedge[n]中权值最小的边
     */
    int min = INT_MAX;
    int i, res;
    for (i = 0; i < n; i++) {
        int lowcost = closedge[i].lowcost;
        if (lowcost > 0 && lowcost < min) {
            min = lowcost;
            res = i;

        }
    }
    return res;
}

void prim(MGraph G, int u) {
    // u是顶点索引，而不是值 书本上的是char类型的值, low_cost中的adjvex也是int, 而树上的也是值.
    int k = u;
    Closedge closedge[n];
    closedge[k].lowcost = 0;
    for (int i = 0; i < G.vex_num; ++i) {
        if (i != k) closedge[i] = {k, G.arcs[k][i]};
    }
    // 将第一个加入的顶点赋值为0
    for (int i = 1; i < G.vex_num; ++i) { // 1 ~ G.vex_num-1
        k = minimum(closedge);    // 获取closedge中最小的
        printf("加入的边为:(%c-%c) \n", G.vertex[closedge[k].adjvex], G.vertex[k]);
        closedge[k].lowcost = 0;
        for (int j = 0; j < G.vex_num; ++j) {    // 更新closedge中的权值
            if (G.arcs[k][j] < closedge[j].lowcost) {
                closedge[j] = {k, G.arcs[k][j]};
            }
        }
    }


}

// 7. 拓扑排序
int indegree[n];

void findInDegree(ALGraph G) {
    for (int i = 0; i < G.vex_num; ++i) {
        indegree[i] = 0;
    }

    for (int i = 0; i < G.vex_num; ++i) {
        for (ArcNode *p = G.adjList[i].firstArc; p != nullptr; p = p->nextArc) {
            indegree[p->adjvex]++;
        }
    }

}

int TopologicalSort(ALGraph G) {
    findInDegree(G);
    stack<int> S;
    // 先把入度为0的点放入栈中
    for (int i = 0; i < G.vex_num; ++i) {
        if (indegree[i] == 0) S.push(i);
    }
    int count = 0;
    while (!S.empty()) {
        int vex = S.top();
        S.pop();
        printf("%d\t", vex);
        count++;
        for (ArcNode *p = G.adjList[vex].firstArc; p != nullptr; p = p->nextArc) {
            int v = p->adjvex;
            if (!(--indegree[v])) { // ★
                S.push(v);
            }
        }
    }
    if (count != G.vex_num) return 0;
    return 1;
}


int main() {
    MGraph MG = createMGraph(a1);
    ALGraph AG;
    AG = MGraph2ALGraph(MG, AG);
    printf("DFS:\n");
    DFS(AG, 0);
    printf("\nBFS:\n");
    BFSTraverse(AG);
    init_visited();
    printf("\nfind_path:\n");
    vector<int> path;
    find_path(AG, 4, 1, path);

    // 无向有权图
    MGraph MG2 = createMGraph(a2);
    printf("\nprim:\n");
    prim(MG2, 2);

    // DAG
    MGraph MG3 = createMGraph(a3);
    ALGraph AG3 = MGraph2ALGraph(MG3, AG);
    printf("TopologicalSort:\n");
    TopologicalSort(AG3);
}
