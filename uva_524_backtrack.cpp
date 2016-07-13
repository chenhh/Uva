/**
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/5/524.pdf
0<n<=16, the max sum is 31 (16+15)
**/

#include <cstdio>
#include <cstring>
using namespace std;

bool sieves[] = {
    0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0
};
int ring[16];
bool chosen[16];

void dfs(int n, int pos){
    int idx;
    if (pos == n){
        if (sieves[ring[pos-1] + ring[0]]){
            for(idx=0; idx<n-1; ++idx)
                printf("%d ", ring[idx]);
            printf("%d\n", ring[n-1]);
        }
        return;
    }

    for(idx=1; idx<n; ++idx){
        if (!chosen[idx] && sieves[ring[pos-1]+ idx +1]){
            chosen[idx] = true;
            ring[pos] = idx+1;
            dfs(n, pos+1);
            chosen[idx] = false;
        }
    }
}

int main(){
    int n, n_case=0;
    while (scanf("%d", &n) == 1){
        if (n_case)
            printf("\n");
        printf("Case %d:\n", ++n_case);
        memset(chosen, 0, sizeof(chosen));
        memset(ring, 0, sizeof(ring));
        ring[0] = 1;
        chosen[0] = true;
        dfs(n, 1);
    }

}
