/*
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: C++ AC, python TLE
difficulty: 1
https://uva.onlinejudge.org/external/116/11660.pdf

x1 = 1
x2 = 11 (one 1)
x3 = 21 (two 1s)
x4 = 1211 (one 2, two 1s)
x5 = 111221 (one 1, one 2, two 1s)
x6 = 312211 (three 1s, two 2s, one 1)
x7 = 13112221 (one 3, one 1, two 2s, two 1s)
*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int i, j, idx, jdx;
    string str[1000+10];
    stringstream ss;
    // speed up c++ io performance
    std::ios::sync_with_stdio(false);

    while(cin >> str[0] >> i>> j) {
        if ( str [0] == "0" && i == 0 && j == 0 )
            break;
        str[0] += '-';

        for (idx=1; idx<i; ++idx) {
            int cnt = 1;
            str[idx] = "";
            for (jdx=0; jdx < str[idx-1].size()-1 && jdx<=1000; ++jdx) {
                if (str[idx-1][jdx] == str[idx-1][jdx+1])
                    ++cnt;
                else {
                    ss << cnt;
                    str[idx] += ss.str();
                    str[idx] += str[idx-1][jdx];
                    // clear stringstream content
                    ss.str("");
                    cnt = 1;
                }
            }
            str[idx] += '-';
        }
        cout<<str[i-1][j-1]<<endl;
    }
    return 0;
}
