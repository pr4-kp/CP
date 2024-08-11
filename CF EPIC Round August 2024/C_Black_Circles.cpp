#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <vector>

#ifndef ONLINE_JUDGE
#include "template.cpp"
#else
#define debug(...)
#define debugArr(...)
#endif

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

ll dist(ll sx, ll sy, ll ex, ll ey) {
    return (sx - ex) * (sx - ex) + (sy - ey) * (sy - ey);
}

void solve() {
    int n;
    cin >> n;
    vector<pair<ll, ll>> p(n);

    for (int i = 0; i < n; ++i) {
        ll x, y;
        cin >> x >> y;
        p[i] = {x, y};
    }

    ll sx, sy, ex, ey;
    cin >> sx >> sy >> ex >> ey;

    ll d = dist(sx, sy, ex, ey);

    for (int i = 0; i < n; ++i) {
        if (dist(p[i].first, p[i].second, ex, ey) <= d) {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
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