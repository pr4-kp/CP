#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <unordered_map>
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
    int n;
    cin >> n;
    vector<ll> a(n);
    vector<bool> added(n, false);
    vector<pair<int, int>> edges(n - 1);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << "YES\n";

    for (ll i = n - 1; i >= 1; ++i) {
        // add edge if two things have the same residue mode i
        // remove the first one from possible things to check

        unordered_map<ll, int, custom_hash> seen;
        ll a1 = -1LL, a2 = -1LL;
        for (int j = 0; j < n; ++j) {
            if (!added[j]) {
                if (seen.contains(a[j] % i)) {
                    a1 = j;
                    a2 = seen[a[j] % i];
                    break;
                } else {
                    seen[a[j] % i] = j;
                }
            }
        }

        cout << a1 << " " << a2 << "\n";
        edges[i - 1] = {a1, a2};
        added[a1] = true;
    }

    for (auto e : edges) {
        cout << e.first << " " << e.second << "\n";
    }
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