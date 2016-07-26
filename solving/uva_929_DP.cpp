/***
# -*- coding: utf-8 -*-
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/9/929.pdf
***/

#include <cstdio>
#include <cstdlib>
using namespace std;

int maze[1001][1001], cost[1001][1001];

inline int min(int a, int b){
    return a<=b ? a: b;
}

int min_travrsal(const int n_row, const int n_col){
    /***
    cost[idx][jdx] = min(
            cost[idx-1][jdx] + maze[idx][jdx],   // from upper
            cost[idx][jdx-1] + maze[idx][jdx],   // from left
    )
    ***/
    int idx, jdx;

    //initial condition
    cost[0][0] = maze[0][0];
    for(jdx=1; jdx<n_col; ++jdx)
        cost[0][jdx] = maze[0][jdx] + cost[0][jdx-1];

    for(idx=1; idx<n_row; ++idx)
        cost[idx][0] = maze[idx][0] + cost[idx-1][0];

    // DP
    for(idx=1; idx<n_row; ++idx)
        for(jdx=1; jdx<n_col; ++jdx)
            cost[idx][jdx] = min(cost[idx][jdx-1] + maze[idx][jdx],
                                 cost[idx-1][jdx]+ maze[idx][jdx]);

    return cost[n_row-1][n_col-1];
}


int main(){
    int n_maze, n_row, n_col, idx, jdx;
    scanf("%d", &n_maze);
    while (n_maze--){
        scanf("%d", &n_row);
        scanf("%d", &n_col);

        for(idx=0; idx<n_row; ++idx)
            for (jdx=0; jdx<n_col; ++jdx)
                scanf("%d ", &maze[idx][jdx]);

        printf("%d\n", min_travrsal(n_row, n_col));
    }
    return EXIT_SUCCESS;
}
