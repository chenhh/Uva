/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11714.htm
https://uva.onlinejudge.org/external/117/11714.pdf
*/
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    unsigned long long n;
    while (cin>>n) {
        cout<<(n-1) + (int)(log(n - 1) / log(2))<<endl;
    }
    return 0;
}
