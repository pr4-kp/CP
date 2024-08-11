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

/*
If, at any time, Bob removes something that Alice did not remove,
she wins.

Obs. If the oustide elements match throughout the game, Alice will lose because Bob can always match

Cl. If the arrays are equal or reverses of each other, Bob can win
Cl. Otherwise, Alice can win
Pf. Suppose p_i reveals p_(i-1) but it doesnt for Bob. Then alice removes p_(i-1), and Bob removes something different.
If they were matching the whole time (this is optimal for Bob), then Alice just has to preseve the value Bob removed
*/

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    int eq = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] == b[i]) {
            eq++;
        }
    }

    if (eq == n) {
        cout << "Bob\n";
        return;
    }

    eq = 0;

    for (int i = 0; i < n; ++i) {
        if (a[i] == b[n - i - 1]) {
            eq++;
        }
    }

    if (eq == n) {
        cout << "Bob\n";
        return;
    }

    cout << "Alice\n";
    return;
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