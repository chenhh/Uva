/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/17/1709.pdf
maximum drop down

correct but TLE, since the python loop is very slow
*/

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


int main(){
    int p, a,b,c,d,n, k;
    double peak, mad, price, diff;

    std::ios::sync_with_stdio(false);

    while(cin>>p>>a>>b>>c>>d>>n){
        mad = 0, peak = 0, mad = 0, diff = 0;
        for (k=1; k<=n; ++k){
            price = p * (sin(a * k + b) + cos(c * k + d) + 2);
            if (price > peak)
                peak = price;
            diff = peak - price > 0 ? peak - price : price - peak;
            if (diff > mad)
                mad = diff;
        }
        cout<<fixed<<setprecision(6)<<mad<<endl;
    }
    return 0;
}
