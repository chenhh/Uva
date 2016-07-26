/***
# -*- coding: utf-8 -*-
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/9/929.pdf
Dijkstra algorithm
***/

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <queue>
using namespace std;
const int ARR_SIZE = 1000;
const int GRAPH_SIZE = ARR_SIZE * ARR_SIZE;

int maze[ARR_SIZE][ARR_SIZE], dist[ARR_SIZE][ARR_SIZE];
bool visited[ARR_SIZE][ARR_SIZE];

// upper, right, lower, left
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

struct Node {
    // (x,y) and the candidate dist from source.
    int x, y, d;
};

bool operator<(const Node& lhs, const Node& rhs)
{
    // overloading less operator of node
    return lhs.d > rhs.d;
}

int dijkstra(const int n_row, const int n_col)
{
    int idx, jdx;
    // the queue keeps the dist of all visited nodes
    priority_queue<Node> min_heap;

    // initialize
    for(idx=0; idx<n_row; ++idx) {
        for(jdx=0; jdx<n_col; ++jdx) {
            visited[idx][jdx] = false;
            dist[idx][jdx] = INT_MAX;
        }
    }
    dist[0][0] = maze[0][0];
    min_heap.push(Node{0, 0, dist[0][0]});

    Node node;
    int bypass, kdx, cur_x, cur_y;
    while(!min_heap.empty()){
        // the visited node with the current minimal dist from source.
        node = min_heap.top();
        min_heap.pop();
        visited[node.x][node.y] = true;

        // traversal the unvisited connected nodes
        for (kdx=0; kdx<4; ++kdx){
            cur_x = node.x+dx[kdx];
            if (cur_x < 0 || cur_x >= n_row)
                continue;

            cur_y = node.y+dy[kdx];
            if (cur_y <0 || cur_y >= n_col)
                continue;

            if (visited[cur_x][cur_y])
                continue;
            //printf("child (%d %d)\n", cur_x, cur_y);
            bypass = dist[node.x][node.y] + maze[cur_x][cur_y];
            if (bypass < dist[cur_x][cur_y]){
                dist[cur_x][cur_y] = bypass;
                min_heap.push(Node{cur_x, cur_y, bypass});
            }
        }
    }
    return dist[n_row-1][n_col-1];
}

int main()
{
    int n_maze, n_row, n_col, idx, jdx;
    scanf("%d", &n_maze);
    while (n_maze--) {
        scanf("%d", &n_row);
        scanf("%d", &n_col);

        // read matrix
        for(idx=0; idx<n_row; ++idx)
            for (jdx=0; jdx<n_col; ++jdx)
                scanf("%d", &maze[idx][jdx]);

        printf("%d\n", dijkstra(n_row, n_col));
    }
    return EXIT_SUCCESS;
}
