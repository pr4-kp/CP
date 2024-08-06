#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <vector>

using namespace std;
using ll = long long;

static uint64_t x;

uint64_t next() {
    uint64_t z = (x += 0x9e3779b97f4a7c15);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9;
    z = (z ^ (z >> 27)) * 0x94d049bb133111eb;
    return z ^ (z >> 31);
}
/**
 * Use with
 * unordered_map<long long, int, custom_hash> safe_map;
 * gp_hash_table<long long, int, custom_hash> safe_hash_table;
 * so you don't get hacked :(
 */
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m, 0));
    vector<vector<int>> b(n, vector<int>(m, 0));

    string s;
    for (int i = 0; i < n; ++i) {
        cin >> s;
        for (int j = 0; j < m; ++j) {
            a[i][j] = (int)s[j] - '0';
        }
    }
    for (int i = 0; i < n; ++i) {
        cin >> s;
        for (int j = 0; j < m; ++j) {
            b[i][j] = (int)s[j] - '0';
        }
    }

    for (int i = 0; i < n; ++i) {
        int cmp1 = 0, cmp2 = 0;
        for (int j = 0; j < m; ++j) {
            cmp1 += a[i][j];
            cmp2 += b[i][j];
        }
        if ((cmp1 - cmp2) % 3 != 0) {
            cout << "NO\n";
            return;
        }
    }

    for (int j = 0; j < m; ++j) {
        int cmp1 = 0, cmp2 = 0;
        for (int i = 0; i < n; ++i) {
            cmp1 += a[i][j];
            cmp2 += b[i][j];
        }
        if ((cmp1 - cmp2) % 3 != 0) {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
    return;
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