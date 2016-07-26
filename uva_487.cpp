/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

487 Boggle Blitz

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/487.pdf
***/
#include <cstdio>
#include <set>
#include <string>
#include <algorithm>

using namespace std;
char board[21][21], tmp[401];
bool visited[21][21] = {};
set<string> ans;

void dfs(int x, int y, const int n_char, int idx) {
    if(idx >= 3) {
        tmp[idx] = '\0';
        ans.insert(tmp);
    }
    // out of boundary
    if(x < 0 || y < 0 || x >= n_char || y >= n_char)
        return;

    // non-increasing
    if(idx > 0 && board[x][y] <= tmp[idx-1])
        return;

    // visited
    if(visited[x][y])
        return;

    tmp[idx] = board[x][y];
    visited[x][y] = true;
    dfs(x+1, y, n_char, idx+1);
    dfs(x-1, y, n_char, idx+1);
    dfs(x, y+1, n_char, idx+1);
    dfs(x, y-1, n_char, idx+1);
    dfs(x-1, y-1, n_char, idx+1);
    dfs(x-1, y+1, n_char, idx+1);
    dfs(x+1, y+1, n_char, idx+1);
    dfs(x+1, y-1, n_char, idx+1);
    visited[x][y] = false;
}
bool cmp(string a, string b) {
    return a.length() < b.length();
}
int main() {
    int n_case, idx, jdx, n_char;
    scanf("%d", &n_case);
    while(n_case--) {
        scanf("%d", &n_char);
        for(idx = 0; idx < n_char; ++idx)
            scanf("%s", board[idx]);

        ans.clear();

        for(idx = 0; idx < n_char; ++idx) {
            for(jdx = 0; jdx < n_char; ++jdx) {
                dfs(idx, jdx, n_char, 0);
            }
        }
        string output[50000];
        int odx = 0;
        for (auto &msg : ans){
            output[odx++] = msg;
        }

        stable_sort(output, output+odx, cmp);
        for(idx = 0; idx < odx; ++idx)
            printf("%s\n", output[idx].c_str());
        if(n_case)
            printf("\n");
    }
    return 0;
}
