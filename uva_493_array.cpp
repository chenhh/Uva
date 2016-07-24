/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/493.pdf
http://luckycat.kshs.kh.edu.tw/homework/q493.htm

rational numbers are countable.
then b/a can be mapping to a unique positive integer.

N:1, E:1,
S:2, W:2,
N:3, E:3,
S:4, W:4,
N:5, E:5,
S:6, W:6,
...
an rational: y/x
***/

#include <cstdio>
using namespace std;

const int ARR_SIZE = 500001;
int arr_x[ARR_SIZE] = {};
int arr_y[ARR_SIZE] = {};

// record the visited rational numbers.
bool rational[1500][1500];

int gcd(const int x, const int y) {
    // rational y/x
    int a = x>0 ? x: -x;
    int b = y>0 ? y: -y;
    int tmp;

    while (a%b){
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return b;
}

bool is_valid_rational(int x, int y){
    if (x ==0 || y ==0 || x == y)
        // zero and one has been visited
        return false;

    int com = gcd(x, y);
    if (com != 1){
        // not relative prime
        x /= com;
        y /= com;
    }
    if (x<0){
        x = -x;
        y = -y;
    }

    if (!rational[x+750][y+750]){
        // the rational was not visited before
        rational[x+750][y+750] = true;
        return true;
    } else {
        return false;
    }
}


int main() {
    arr_x[0] = 1;
    arr_y[0] = 1;
    rational[1+750][1+750] = true;
    arr_x[1] = 1;
    arr_y[1] = 0;
    rational[1+750][0+750] = true;

    int idx=2, cnt=0, jdx;
    int curr_x =0, curr_y = 0;
    while (idx < ARR_SIZE){
        if (cnt %2){
            // north
            for (jdx=1; jdx<=cnt+1; ++jdx){
                ++curr_y;
                if (is_valid_rational(curr_x, curr_y)){
                    //printf("[%d] %d/%d\n", idx, curr_y, curr_x);
                    arr_x[idx] = curr_x;
                    arr_y[idx] = curr_y;
                    ++idx;
                }

                if (idx >= ARR_SIZE)
                    break;
            }
            // east
             for (jdx=1; jdx<=cnt+1; ++jdx){
                ++curr_x;
                if (is_valid_rational(curr_x, curr_y)){
                    //printf("[%d] %d/%d\n", idx, curr_y, curr_x);
                    arr_x[idx] = curr_x;
                    arr_y[idx] = curr_y;
                    ++idx;
                }

                if (idx >= ARR_SIZE)
                    break;
            }

        } else {
            // south
             for (jdx=1; jdx<=cnt+1; ++jdx){
                --curr_y;
                if (is_valid_rational(curr_x, curr_y)){
                    //printf("[%d] %d/%d\n", idx, curr_y, curr_x);
                    arr_x[idx] = curr_x;
                    arr_y[idx] = curr_y;
                    ++idx;
                }

                if (idx >= ARR_SIZE)
                    break;
            }

            // west
             for (jdx=1; jdx<=cnt+1; ++jdx){
                --curr_x;
                if (is_valid_rational(curr_x, curr_y)){
                    //printf("[%d] %d/%d\n", idx, curr_y, curr_x);
                    arr_x[idx] = curr_x;
                    arr_y[idx] = curr_y;
                    ++idx;
                }

                if (idx >= ARR_SIZE)
                    break;
            }
        }
        // update
        ++cnt;
    }

    int kdx;
    while (scanf("%d", &kdx)== 1){
        int x_val = arr_x[kdx];
        int y_val = arr_y[kdx];

        if (x_val < 0)
            printf("%d / %d\n", -y_val, -x_val);
        else
            printf("%d / %d\n", y_val, x_val);
    }

}
