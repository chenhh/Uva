/***
# -*- coding: utf-8 -*-
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

294 Divisors

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/294.pdf

8 = 2^3, the number of divisor is (3+1) = 4
6= 2*3, the number of divisor is (1+1)*(1+1) = 4
40 = 2^3*5, the number of divisors is (3+1)*(1+1) = 8

***/

#include <cstdio>
#include <vector>
using namespace std;

const int UPPER = 1000000001;
const int SQRT_UPPER = 31650;

// false: is a prime, true: no a prime
// 0 and 1 are treated as primes
bool sieves[SQRT_UPPER] = {};
vector<int> primes;

void linear_sieve(){
    int idx, jdx;
    for (idx=2; idx<SQRT_UPPER; ++idx){
        if (!sieves[idx])
            primes.push_back(idx);

        for(jdx=0; idx*primes[jdx]<SQRT_UPPER; ++jdx){
            sieves[idx*primes[jdx]] = true;
            if (idx % primes[jdx] == 0)
                break;
        }
    }
}

int factorization(int value){
    int idx, cnt = 1, exp;
    for(idx=0; primes[idx]*primes[idx]<=value; ++idx){
        exp = 0;
        if (value % primes[idx] == 0){
            while(value % primes[idx] == 0){
                value /= primes[idx];
                ++exp;
            }
            cnt *= (exp+1);
        }
    }
    if (value != 1)
        cnt *= 2;
    return cnt;
}

int main(){
    int n_case =0;
    int l, u, idx, jdx, max_value, max_divisor;
    linear_sieve();

    scanf("%d", &n_case);
    for (idx=0; idx<n_case; ++idx){
        scanf("%d %d", &l, &u);
        max_value = l;
        max_divisor = 0;
        for(jdx=l; jdx<=u; ++jdx){
            int n_divisor = factorization(jdx);
            if (n_divisor > max_divisor){
                max_divisor = n_divisor;
                max_value = jdx;
            }
        }
        printf("Between %d and %d, %d has a maximum of %d divisors.\n",
               l, u, max_value, max_divisor);
    }
    return 0;
}
