#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int p, n;
    int ans = -1;
    cin >> p >> n;
    unordered_set<string> a;

    for (int i = 0; i < n; ++i) {
        string part;
        cin >> part;
        a.insert(part);
        if (a.size() == p && ans == -1) {
            ans = i + 1;
        }
    }

    if (ans != -1) {
        cout << ans << "\n";
    } else {
        cout << "paradox avoided\n";
    }
}