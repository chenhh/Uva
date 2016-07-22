#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <cstdlib>
using namespace std;

typedef long long ll;

 // bruce force
ll maxProduct(const vector<int> &data){
    ll maxprod = 0, prod;
    int i, j, len = data.size();

    for(i=0; i<len; ++i){
        prod = 1;
        for(j=i; j<len; ++j){
            prod *= data[j];
            if(prod > maxprod)
                maxprod = prod;
        }
    }
    return maxprod;
}

int main(){
    int N, i, cnt = 0;
    int S[18] ={0};
    int value, maxprod;
    string input;
    vector<int> data;

    while(scanf("%d ", &N) == 1){
        getline(cin, input);
        istringstream iss(input);
        data.clear();
        for(i=0 ;i<N; ++i){
            iss>>value;
            data.push_back(value);
        }
        //copy(data.begin(), data.end(), ostream_iterator<int>(cout, " "));
       cout<<"Case #"<<(++cnt)<<": The maximum product is "<<maxProduct(data)<<".\n\n";
    }
    return EXIT_SUCCESS;
}
