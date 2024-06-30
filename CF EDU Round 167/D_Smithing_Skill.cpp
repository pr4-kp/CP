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

vector<ll> dp(1000001LL, -1);
ll fill(ll i) {
    dp[i] = ;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll n, m;
    ll exp = 0;
    cin >> n >> m;

    vector<ll> a(n);
    vector<ll> b(n);
    vector<tuple<ll, ll, ll>> diffs(n);

    vector<ll> c(m);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
        diffs[i] = {a[i],
                    b[i],
                    a[i] - b[i]};
    }

    auto cmp = [](const tuple<ll, ll, ll> a, const tuple<ll, ll, ll> b) {
        return get<2>(a) < get<2>(b);
    };

    sort(diffs.begin(), diffs.end(), cmp);
    ll mindiff = get<2>(diffs[0]);
    cout << mindiff << endl;

    for (int i = 0; i < m; ++i) {
        cin >> c[i];
        if (c[i] > 1000000LL) {
            ll v = ((c[i] - 1000000LL + mindiff - 1) / mindiff);
            c[i] -= (ll)v * mindiff;
            exp += v * 2;
        }
    }

    for (ll i = 1000000LL; i >= 0; --i) {
        if (dp[i] == -1) {
            fill(i);
        }
    }

    cout << exp << endl;
}