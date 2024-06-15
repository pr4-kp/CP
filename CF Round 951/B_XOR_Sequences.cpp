#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
using ll = long long;

void solution()
{
    ll x, y;
    cin >> x >> y;

    cout << (1 << __builtin_ctz(x-y)) << endl;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        solution();
    }
}