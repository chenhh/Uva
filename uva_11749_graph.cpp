/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/117/11749.pdf
*/

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

#define max_node 501
#define N_INF -2147483648
class Node {
public:
   int node, ppa;
   Node(int _node, int _ppa):node(_node), ppa(_ppa) {
   }
};

int n, max_ppa;
vector<Node> graph[max_node];
bool visited[max_node];

int DFS(int n1) {
   int count = 1;
   for (int idx=0, size=graph[n1].size(); idx<size; idx++) {
        int n2 = graph[n1][idx].node, ppa = graph[n1][idx].ppa;
      if (visited[n2] || ppa!=max_ppa)
        continue;
      visited[n2] = true;
      count += DFS(n2);
   }
   return count;
}

main() {
    int n_node, n_edge, idx;
    while (scanf("%d %d", &n_node, &n_edge) && (n_node || n_edge)) {
        // initialize
        for (idx=1; idx<=n_node; ++idx){
            graph[idx].clear();
            visited[idx] = false;
        }
        max_ppa = N_INF;
        int n1, n2, ppa;
        while (n_edge--) {
             scanf("%d %d %d", &n1, &n2, &ppa);
             graph[n1].push_back(Node(n2, ppa));
             graph[n2].push_back(Node(n1, ppa));
             max_ppa = max(max_ppa, ppa);
        }
        int ans = 0;
        for(idx=1; idx<=n_node; ++idx){
            if (!visited[idx]){
                visited[idx] = true;
                ans = max(ans, DFS(idx));
             }
        }
        printf("%d\n", ans);
   }
   return 0;
}
