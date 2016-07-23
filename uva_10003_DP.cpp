/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/100/10003.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10003.htm

dynamic programming
***/

#include<cstdio>
#include<climits>
using namespace std;

int cost[52][52];
int cuts[52];

int min_cut(int n_cut){
    // n_cut: the number of element in cuts,
    // it contains two end points.
    int idx, jdx, kdx, n_pt, bypass;

    // initialize
    for(idx=0; idx<n_cut-1; ++idx)
        cost[idx][idx+1] = 0;

    for(n_pt=2; n_pt<n_cut; ++n_pt){
        for (idx=0; idx<=n_cut-n_pt; ++idx){
            jdx = idx +n_pt;
            cost[idx][jdx] = INT_MAX;

            for(kdx=idx+1; kdx<jdx; ++kdx){
                bypass = cost[idx][kdx]+cost[kdx][jdx]+cuts[jdx]-cuts[idx];
                cost[idx][jdx] = cost[idx][jdx]< bypass ? cost[idx][jdx]: bypass;
            }
        }
    }
    return cost[0][n_cut-1];
}

int main() {
    int stick_len, n_cut, idx, ans;

    while (scanf("%d", &stick_len) && stick_len){
        scanf("%d", &n_cut);
        cuts[0] = 0;
        for(idx=1; idx<=n_cut; ++idx)
            scanf("%d", &cuts[idx]);
        cuts[n_cut+1] = stick_len;
        ans = min_cut(n_cut+2);
        printf( "The minimum cutting is %d.\n", ans);
    }

    return 0;
}
