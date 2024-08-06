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
    ll ans = 0;
    cin >> n >> m;
    vector<pair<ll, ll>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first; // number of petals
    }
    for (int i = 0; i < n; i++) {
        cin >> a[i].second; // amount of flowers with this many petals
    }

    sort(begin(a), end(a),
         [&](const auto &x, const auto &y) {
             return x.first < y.first;
         });

    ans = max(ans, min(a[0].first * (m / a[0].first), a[0].first * a[0].second));

    for (int i = 0; i < n - 1; i++) {
        ll take_high = min(m / a[i + 1].first, a[i + 1].second);
        ll cr = take_high * a[i + 1].first;
        ans = max(ans, take_high * a[i + 1].first);

        if (a[i + 1].first - a[i].first == 1) {
            if (take_high < a[i + 1].second) {
                take_high++;

                ll can_take_high = a[i + 1].second - take_high;
                if (take_high * a[i + 1].first - min(a[i].second, take_high) <= m) {
                    ans = m;
                    cout << m << "\n";
                    return;
                }
            } else {
                ll take_low = min((m - take_high * a[i + 1].first) / a[i].first, a[i].second);
                ans = max(ans, take_high * a[i + 1].first + take_low * a[i].first);
                if (take_low == a[i].second) {
                    continue;
                } else { // so we have freedom with the low values, but not the high
                    take_low++;
                    ll can_take_low = a[i].second - take_low;

                    if (take_high * a[i + 1].first + take_low * a[i].first - min(can_take_low, take_high) <= m) {
                        ans = m;
                        cout << m << "\n";
                        return;
                    }
                    // cout << take_high * a[i + 1].first + take_low * a[i].first << "\n";
                }
            }
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