#include <bits/stdc++.h>

using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    int ans = 0;
    while (find(a.begin(), a.end(), ans) != a.end())
    {
        ans ++;
    }
    cout << ans << endl;
    return 0;
}