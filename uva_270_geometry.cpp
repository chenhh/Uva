/*
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/270.pdf
http://www.algorithmist.com/index.php/UVa_270
*/
#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

struct Point {
	int x, y;

	Point() {}

	Point(int _x, int _y){
        x = _x;
        y = _y;
    }

    bool operator < (Point P) const{
        if(x!=P.x)
            return x < P.x;
        return y < P.y;
    }
};

int gcd(int x, int y) {
	if(y == 0)
        return x;
	x = abs(x);
	y = abs(y);
	int tmp;
	while(x%y) {
		tmp = x;
		x = y;
        y = tmp%y;
	}
	return y;
}


int main(){
    int T, n;
    cin>>T;
    string line;
    getline(cin, line);
    getline(cin, line);
    Point data[700];
    Point slope[700];
    while(T--){
        n = 0;
        while(getline(cin, line)){
            if(line=="")
                break;
            sscanf(line.c_str(),"%d %d",&data[n].x,&data[n].y);
            ++n;
        }
        int ans = 2, diff_x, diff_y;
        for(int idx = 0;idx<n-1; ++idx){
            for(int jdx = idx+1, kdx = 0;jdx<n; ++jdx){
                diff_x = data[idx].x-data[jdx].x;
                diff_y = data[idx].y-data[jdx].y;
                if(diff_x || diff_y){
                    int g = __gcd(diff_x, diff_y);
                    diff_x /= g;
                    diff_y /= g;
                }
                slope[kdx] = Point(diff_x, diff_y);
                ++kdx;
            }
            sort(slope,slope+(n-1));
            int aux = 1;
            for(int jdx = 1;jdx+1<n;++jdx){
                if(slope[jdx].x!=slope[jdx-1].x || slope[jdx].y!=slope[jdx-1].y)
                    aux = 1;
                else
                    ++aux;
                ans = max(ans, aux+1);
            }
        }
        cout<<ans<<endl;
        if(T>0)
            cout<<endl;
    }
    return 0;
}

