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
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    ll l = 0;
    ll r = 1;
    ll tot = a[0];
    ll ans = 0;
    ll it = 0;

    while (l <= r) {
        if (r == n && l == n) {
            cout << ans << "\n";
            return;
        }
        if (tot <= m && a[r - 1] - a[l] <= 1) { // actually check that the total is valid
            ans = max(ans, tot);
        }
        // if (it > 1000) return;
        // it++;
        // cout << l << " " << r << "\n";
        // if (l >= n || r >= n) return;
        if (r < n && tot + a[r] <= m && a[r] - a[l] <= 1) {
            tot += a[r];
            r++;
        } else {
            tot -= a[l];
            l++;
        }
        if (tot <= m && a[r - 1] - a[l] <= 1) { // actually check that the total is valid
            ans = max(ans, tot);
        }
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