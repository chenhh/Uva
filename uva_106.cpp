/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/106.pdf
http://luckycat.kshs.kh.edu.tw/homework/q106.htm

https://zh.wikipedia.org/zh-tw/%E5%8B%BE%E8%82%A1%E5%AE%9A%E7%90%86

x^2 + y^2 = z^2
given (m,n) are positive integers.
x = m^2 - n^2
y= 2mn
z = m^2 + n^2

***/


#include <cstdio>
#include <cstring>
using namespace std;

const int UPPER = 1000000;
int used[UPPER];

int gcd(int x, int y){
    int tmp;
    while (x % y){
        tmp = x;
        x = y;
        y = tmp % y;
    }
    return y;
}


int main(){
    int val, m, n, m2, n2, x, y, z;

    while (scanf("%d", &val) == 1) {
        int n_rp_sol = 0;
        memset(used, 0, sizeof(used));

        for(m=1; m<1000; ++m){
            for (n=m+1; ;n+=2){
                if (gcd(m, n)!= 1)
                    continue;

                m2 = m * m;
                n2 = n * n;
                x = n2 - m2;
                y = 2*m*n;
                z= n2 + m2;

                if (z >val)
                    break;

                ++n_rp_sol;

                int kx=x, ky=y, kz=z;
                while (kz <= val){
                    used[kx-1] = 1;
                    used[ky-1] = 1;
                    used[kz-1] = 1;
                    kx += x;
                    ky += y;
                    kz += z;
                }
            }
        }
        int not_used_num = val;
        for (int idx=0; idx<val; ++idx)
            not_used_num -= used[idx];

        printf("%d %d\n", n_rp_sol, not_used_num);
    }

    return 0;
}
