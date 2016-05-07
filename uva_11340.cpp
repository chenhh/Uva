/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/113/11340.pdf
*/
#include<iostream>
#include <iomanip>
#include<map>
#include<string>
using namespace std;

int main(){
    int T, K, M, value;
    char letter;
    string line;

    cin >>T;
    map<char, int> m;

    for(int t=0; t<T; t++){
        cin >>K;
        m.clear();
        int price;

        for(int k = 0; k<K; k++){
            cin >>letter>>value;
            m[letter] = value;
        }

        cin >> M;
        cin.get();
        double pay=0;
        for (int r=0; r<M; r++){
            getline(cin, line);
            for (int j=0; j<line.size() ; j++) {
                if (m[line[j]])
                    pay+=m[line[j]];
            }
        }
        cout<<setprecision(2)<<fixed<<(pay/100.0)<<"$"<<endl;
    }
    return 0;
}
