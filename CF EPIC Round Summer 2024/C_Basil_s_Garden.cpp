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
    int n;
    cin >> n;
    vector<ll> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << a[0] << endl;
        return;
    }
    reverse(a.begin(), a.end());

    ll t = 0;
    t += a[0]; // guarantees that a_(n-1) is zero at this point
    a[0] = 0;

    for (int i = 1; i < n; ++i) {
        if (a[i] - t > a[i - 1]) {
            t += a[i] - t;
            a[i] = 0;
        } else {
            t += 1;
            a[i] = 0;
        }
    }

    cout << t << endl;

    // ll m = a[0];
    // ll t = 0;
    // for (int i = 1; i < n; ++i) {
    //     // keep the max if decreasing
    //     if (a[i - 1] > a[i]) {
    //         continue;
    //     } else {
    //         t += m;
    //         m = a[i];
    //     }
    // }

    // if (a[n - 2] > a[n]) {
    //     t += m;
    // }
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