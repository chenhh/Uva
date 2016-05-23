/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: C++ AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11526.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11526.htm
"""
*/

#include <iostream>
#include <cmath>
using namespace std;

long long H(int n)
{
    int root = int(sqrt(n)) + 1;
    long long res = 0;
    for(int i=1; i < root; ++i)
        res += n/i;
    --root;
    res = 2*res - root*root;
    return res;
}

int main() {
    int cases, n;
    cin>>cases;
    while(cases--) {
        cin>>n;
        cout<<H(n)<<endl;
    }
    return 0;

}
