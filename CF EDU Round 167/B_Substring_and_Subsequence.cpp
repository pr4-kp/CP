#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int match(string a, string b, int i) {
    int n = a.size();
    int m = b.size();
    int k = i;
    int out = 0;
    for (int j = 0; j < n; ++j) {
        if (k > m) {
            return out;
        }
        if (a[j] == b[k]) {
            k += 1;
            out += 1;
        }
    }
    return out;
}

void solve() {
    string a, b;
    cin >> a >> b;

    int n = b.size();
    int m = 0;

    for (int i = 0; i < n; ++i) {
        m = max(m, match(a, b, i));
    }

    cout << a.size() + n - m << endl;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}