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
    for (size_t i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (size_t i = 0; i < n; i++) {
        if ((a[i] - a[0]) % 2 != 0) {
            cout << "-1\n";
            return;
        }
    }

    vector<ll> na(n);
    vector<ll> ans = vector<ll>();
    ll mi = *min_element(a.begin(), a.end()), ma = *max_element(a.begin(), a.end());
    ll av = 1;
    while (av != 0) {
        mi = *min_element(a.begin(), a.end());
        ma = *max_element(a.begin(), a.end());
        av = (mi + ma) / 2LL;

        ans.push_back(av);

        for (size_t i = 0; i < n; i++) {
            a[i] = abs(a[i] - av);
        }
    }

    cout << ans.size() - 1 << "\n";
    for (size_t i = 0; i < ans.size() - 1; i++) {
        cout << ans[i] << " ";
    }
    cout << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--)
        solve();
}