/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/111/11136.pdf
*/

#include <iostream>
#include <set>
using namespace std;

int n, x, k;
long long sum;
multiset<int> bills;

int main() {
    std::ios::sync_with_stdio(false);
    while(cin >> n && n) {
        sum = 0;
        bills.clear();
        for(int idx=0; idx<n; ++idx) {
            cin >> k;
            for(int jdx=0; jdx<k; ++jdx) {
                cin >> x;
                bills.insert(x);
            }
            multiset<int>::iterator hit = bills.end(), lot = bills.begin(); hit--;
            sum += (*hit)-(*lot);
            bills.erase(hit);
            bills.erase(lot);
        }
        cout << sum <<endl;
    }
    return 0;
}
