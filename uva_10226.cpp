/*
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1
https://uva.onlinejudge.org/external/102/10226.pdf
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
using namespace std;

int main()
{
    string dummy;
    int number_of_cases;
    cin >> number_of_cases;
    getline(cin, dummy);
    getline(cin, dummy);
    for (int idx = 0; idx < number_of_cases; idx++)
    {
        map<string, int> tree_count;
        int count = 0;
        while (true) {
            string tree;
            getline(cin, tree);
            if (tree.length() == 0) {
                break;
            }
            map<string, int>::iterator probe = tree_count.find(tree);
            if (probe == tree_count.end())
                tree_count.insert(pair<string, int>(tree, 1));
            else
                tree_count[tree]++;
            count++;
        }
        double factor = 100.0 / count;
        cout << setprecision(4) << fixed;
        map<string, int>::iterator iter;
        for ( iter= tree_count.begin(); iter != tree_count.end(); iter++){
            cout << iter->first << " " <<iter->second * factor << endl;
        }

        if (idx != number_of_cases - 1)
            cout << endl;
    }
    return 0;
}
