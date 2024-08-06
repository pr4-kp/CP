#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <unordered_set>
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
    ll ans = 0;
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        ans += a[i];
    }

    unordered_set<ll, custom_hash> s;
    vector<ll> h(n, 0LL);

    for (ll i = 0; i < n; ++i) {
        if (s.contains(a[i])) {
            h[i] = max(h[i - 1], a[i]);
        } else {
            if (i > 0) {
                h[i] = h[i - 1];
            }
            s.insert(a[i]);
        }
        ans += h[i];
        // cout << h[i] << " ";
    }
    // cout << "\n";

    s.clear();

    for (ll i = 0; i < n; ++i) {
        if (s.contains(h[i])) {
            h[i] = max(h[i - 1], h[i]);
        } else {
            s.insert(h[i]);
            if (i > 0) {
                h[i] = h[i - 1];
            }
        }
        // cout << h[i] << " ";
    }
    // cout << "\n";

    ll ct = 1LL;
    for (ll i = n - 1; i >= 1; --i) {
        ans += ct * h[i];
        ct++;
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