#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <numeric>
#include <stdint.h>
#include <string>
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
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<ll>> a(n, vector<ll>(m));
    vector<vector<short>> types(n, vector<short>(m));
    ll off = 0; // how off the mountain is from being nice

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; ++i) {
        string in;
        cin >> in;

        for (int j = 0; j < m; ++j) {
            if (in[j] == '0') {
                types[i][j] = -1;
            } else {
                types[i][j] = 1;
            }
            off += types[i][j] * a[i][j];
        }
    }

    // build the prefix sum array
    vector<vector<ll>> ps(n + 1, vector<ll>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            ps[i][j] = types[i - 1][j - 1] + ps[i - 1][j] +
                       ps[i][j - 1] - ps[i - 1][j - 1];
        }
    }

    // cout << off << endl
    //      << endl;
    // for (int i = 0; i <= n; i++) {
    //     for (int j = 0; j <= m; j++) {
    //         cout << ps[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    // cout << endl;
    ll change = 0; // this is "uninitialized"

    for (int i = k; i <= n; ++i) {
        for (int j = k; j <= m; ++j) {
            // calculate the sum of the mountain from (i-k+1, j-k+1) -> (i,j)
            ll s = ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k];
            if (s != 0) {
                if (change == 0) {
                    change = s;
                } else {
                    change = gcd(change, s);
                }
            }
        }
    }
    if (change == 0) {
        if (off == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    } else {
        if (off % abs(change) == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
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