/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/124/12442.pdf
http://luckycat.kshs.kh.edu.tw/homework/q12442.htm
directed graph, may containing cycle

1
3
1 3
2 3
3 1

ans: 2
***/

#include <cstdio>
#include <cstdlib>
#include <stack>
using namespace std;

const size_t MAX_NODE = 50005;

// the graph
int send[MAX_NODE];

// to store the number of nodes which can be visited
int visited[MAX_NODE];

// to record the nodes in a path
bool cycle_path[MAX_NODE];


int dfs_variant(int n_node)
{
    int start;
    int curr, cycle_length, step;
    int max_visited_node=0, max_node=0;
    stack<int> path;

    for(start=1; start<=n_node; ++start) {
        if(visited[start])
            continue;

        curr = start;
        step = 1;
        visited[curr] = step;
        cycle_path[curr] = true;
        path.push(curr);
        // traversal until a cycle
        while(visited[send[curr]] == 0) {
            curr = send[curr];
            ++step;
            visited[curr] = step;
            cycle_path[curr] = true;
            path.push(curr);
        }
        // if the next node is in the path, then it's a cycle
        // else the next node is just a visited node.
        if (cycle_path[send[curr]]) {
            // all nodes in the cycle has the same length
            ++step;
            cycle_length = step - visited[send[curr]];

            visited[send[curr]] = cycle_length;
            cycle_path[send[curr]] = false;

            while (path.top()!=send[curr]) {
                visited[path.top()] = cycle_length;
                cycle_path[path.top()] = false;
                path.pop();
            }
            // pop the cycle start node
            path.pop();
        }
        // beyond the cycle traceback
        cycle_length = visited[send[curr]];
        while (!path.empty()) {
            ++cycle_length;
            visited[path.top()] = cycle_length;
            cycle_path[path.top()] = false;
            path.pop();
        }
    }
    // preserve the one with smallest number
    for(int idx=1; idx<=n_node; ++idx)
        if (visited[idx]>max_visited_node) {
            max_visited_node = visited[idx];
            max_node = idx;
        }

    return max_node;
}

int main()
{
    int n_case, n_node, idx, src, tgt;
    scanf("%d", &n_case);

    for(int tdx=1; tdx<=n_case; ++tdx) {
        scanf("%d", &n_node);

        // initialize
        for(idx=0; idx<=n_node; ++idx) {
            send[idx] = 0;
            visited[idx] = 0;
        }
        // build graph
        for (idx=0; idx<n_node; ++idx) {
            scanf("%d %d", &src, &tgt);
            send[src] = tgt;
        }
        printf("Case %d: %d\n", tdx, dfs_variant(n_node));

    }
    return EXIT_SUCCESS;
}
