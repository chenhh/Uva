/**
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/103/10344.pdf

the problem requires to visit all combinations to compute the corresponding
values is equal to 23 or not..
**/

#include <cstdio>
using namespace std;

int values[5];
bool possible;
bool chosen[5];

void dfs(int value, int pos) {
    if(value == 23 && pos ==5) {
        possible = true;
        return;
    }
    else {
        for(int idx = 0 ; idx < 5 ; ++idx){
            if(!chosen[idx]){
                chosen[idx] = true;
                dfs(value + values[idx], pos+1);
                dfs(value - values[idx], pos+1);
                dfs(value * values[idx], pos+1);
                chosen[idx] = false;
            }
        }
    }
}

int main(){
    int a,b,c,d,e,i;
     while(scanf("%d%d%d%d%d",&a,&b,&c,&d,&e)){
         if(a==0 && b==0 && c==0 && d==0 && e==0)
            return 0;
         values[0]=a;
         values[1]=b;
         values[2]=c;
         values[3]=d;
         values[4]=e;

         possible = false;
         for(int idx =0 ;idx<5 ; ++idx) {
            chosen[idx] = true;
            dfs(values[idx], 1) ;
            chosen[idx] = false;
         }
         if(possible)
            printf("Possible\n");
         else
            printf("Impossible\n");
    }
    return 0;
}
