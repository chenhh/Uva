/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: python TLE, C++ AC
difficulty: 2

https://uva.onlinejudge.org/external/119/11988.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11988.htm
*/
#include <iostream>
#include <string>
using namespace std;

string string_list(string data){
    int idx;
    int n_char = data.length();
    int* nexts = new int[n_char];
    for(idx=0; idx<n_char; ++idx)
        nexts[idx] = -1;

    int len_list = 0;
    int pre_head = -2, head = -2, tail = -2, curr = -2;
    for(idx=0; idx<n_char; ++idx){
        if (data[idx] == '[')
           // move to pre-head
            curr = -2;
        else if (data[idx] == ']')
            // move to tail
            curr = tail;
        else{
            if (len_list > 0) {
             // some elements in the list
                if (curr != -2) {
                    // insert after current position
                    nexts[idx]= nexts[curr];
                    nexts[curr]=idx;
                    if (curr == tail)
                        tail = idx;
                    curr = idx;
                } else {
                    // insert before head
                    nexts[idx] = head;
                    head =idx;
                    curr = idx;
                }
            } else {
                // first element in the list
                head = idx;
                curr = idx;
                tail = idx;
            }
            // update list size
            len_list++;
        }
    }

    //decode
    curr = head;
    string outputs;
    for(idx=0; idx<len_list; ++idx){
        outputs += data[curr];
        curr = nexts[curr];
        if (curr == -1)
            break;
    }
    delete nexts;
    return outputs;
}

int main(){
    string data;
    while(getline(cin, data)){
        cout <<string_list(data)<<endl;
    }
    return 0;
}
