/*

Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: C++ AC, but python TLE
difficulty: 2

https://uva.onlinejudge.org/external/119/11987.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11987.htm
*/
#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    int n_value, n_cmd;
    int t, p, q, ndx,idx, jdx, tmp, sum;
    int root_p, root_q;
    string cmd, input;
    int root[100010];
    vector<int> set[100010];
    stringstream ss_cmd, ss;

    while(getline(cin, cmd)) {
        // clear stringstream
        ss_cmd.str("");
        ss_cmd.clear();
        ss_cmd<<cmd;
        ss_cmd>>n_value>>n_cmd;

        // initialize
        for(idx=0; idx<n_value; ++idx){
            root[idx] = idx;
            set[idx].clear();
            set[idx].push_back(idx);
        }
        //cout<<"n_value:"<<n_value<<" n_cmd:"<<n_cmd<<endl;
        while(n_cmd--) {
            getline(cin, input);
             // clear stringstream
            ss.str("");
            ss.clear();
            ss<<input;
            ss>>t;

            if (t==1){
                // union
                ss>>p>>q;
                root_p = root[p-1];
                root_q = root[q-1];
                if (root_p == root_q)
                    continue;

                // union smaller set to larger one
                if (set[root_p].size() > set[root_q].size()) {
                    for(idx=0; idx<set[root_q].size(); ++idx){
                        tmp = set[root_q][idx];
                        set[root_p].push_back(tmp);
                        root[tmp] = root_p;
                    }
                    set[root_q].clear();
                } else {
                      for(idx=0; idx<set[root_p].size(); ++idx){
                        tmp = set[root_p][idx];
                        set[root_q].push_back(tmp);
                        root[tmp] = root_q;
                    }
                    set[root_p].clear();
                }

            } else if(t== 2) {
                // move p to the set containing q
                ss>>p>>q;
                root_p = root[p-1];
                root_q = root[q-1];
                if (root_p == root_q)
                    continue;

                vector<int>::iterator iter = set[root_p].begin();
                while (*iter != (p-1)){
                        ++iter;
                }
                set[root_p].erase(iter);
                set[root_q].push_back(p-1);
                root[p-1] = root[q-1];
            }

            else if (t==3) {
                ss>>p;
                root_p = root[p-1];
                sum = 0;
                for (idx=0; idx < set[root_p].size(); ++idx)
                        sum += (set[root_p][idx]+1);

                cout<<set[root_p].size()<<" "<<sum<<endl;
            }
        }

    }
    return 0;
}
