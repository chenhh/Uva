/***
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/103/10311.pdf
***/

#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

const int ARR_SIZE = 100000002;

// false: is a prime, true: not a prime
vector<bool> sieves(ARR_SIZE);
vector<int> primes;
vector<int> primes_rank(ARR_SIZE);
int curr;

void linear_sieve()
{
    int idx, jdx, rank=1;
    for (idx=2; idx<ARR_SIZE; ++idx) {
        if (!sieves[idx]){
            primes.push_back(idx);
            primes_rank[idx] = rank++;
        }

        for(jdx=0; idx*primes[jdx]<ARR_SIZE; ++jdx) {
            sieves[idx*primes[jdx]] = true;
            if (idx % primes[jdx] == 0)
                break;
        }
    }

    sieves[0] = true;
    sieves[1] = true; // not a prime in udebug
}

bool is_primes_sum(const int n)
{
    /*
    12 = 1 + 11(diff: 10)
       = 2 + 10 (diff: 8)
       = 3 + 9 (diff: 6)
       = 4 + 8 (diff: 4)
       = 5 + 7 (diff: 2)
       = 6 + 6 (diff: 0), # search should start from half

    11 = 6 + 5
    */
    if (n<=4)
        // 1, 2, 3, 4 are not sum of two distinct primes.
        return false;

    if (n%2){
        // n is an odd number
        curr = 2;
        if (!sieves[n-2])
            return true;
    }
    else{
        // even number
        curr = n/2-1;

        // curr should be a prime
        while (sieves[curr])
            --curr;
        // printf ("start curr:%d\n", curr);
        for(int rdx = primes_rank[curr]-1; rdx>=0; --rdx){
            curr = primes[rdx];
            // printf("loop curr:%d\n", curr);
            if (!sieves[n-curr])
                return true;
        }
    }
    return false;
}

int main()
{
    linear_sieve();

    int n;
    while(scanf("%d", &n)!= EOF){
        if (is_primes_sum(n))
            printf("%d is the sum of %d and %d.\n", n, curr, n-curr);
        else
            printf("%d is not the sum of two primes!\n", n);
    }
    return EXIT_SUCCESS;
}
