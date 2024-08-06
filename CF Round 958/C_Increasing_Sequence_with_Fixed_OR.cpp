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

// the answer is the number of set bits + 1
// for instance, with 10110, we get the sequence
// 00110
// 10010
// 10100
// 10110

string bit_rep(ll x) {
    string ans = "";
    for (ll i = 63; i >= 0; i--) {
        if (x & (1LL << i)) ans += "1";
        else ans += "0";
    }
    return ans;
}

void solve() {
    ll n;
    cin >> n;
    if (__builtin_popcount(n) == 1) {
        cout << "1\n"
             << n << "\n";
        return;
    }
    cout << __builtin_popcountll(n) + 1 << "\n";
    // cout << bit_rep(n) << "\n";
    string c = bit_rep(n);
    vector<int> indices;

    for (int i = 0; i < 64; ++i) {
        if (c[i] == '1') {
            indices.push_back(i);
        }
    }

    for (auto e : indices) {
        string cp = c;
        cp[e] = '0';
        cout << stoll(cp, nullptr, 2) << " ";
    }
    cout << stoll(c, nullptr, 2) << "\n";

    // cout << stoll(bit_rep(n), nullptr, 2) << "\n";
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