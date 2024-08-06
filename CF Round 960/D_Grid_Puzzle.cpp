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
    ll ans = 0;
    cin >> n;
    vector<int> a(n);

    vector<bool> chose_lower(n, false);
    vector<bool> chose_upper(n, false);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] > 4) {
            ans++;
            a[i] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        if (a[i] >= 1) {
            if (i > 0 && chose_lower[i - 1]) {

            } else {
                chose_lower[i] = true;
                ans++;
            }
        }
        if (a[i] >= 3) {
            if (i > 0 && chose_upper[i - 1]) {

            } else {
                chose_upper[i] = true;
                ans++;
            }
        }

        if (chose_upper[i] && chose_lower[i]) {
            chose_upper[i] = false;
            chose_lower[i] = false;
            ans--;
        }
        // cout << chose_lower[i] << " " << chose_upper[i] << "\n";
    }

    cout << ans << "\n";
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