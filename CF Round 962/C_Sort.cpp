#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <unordered_map>
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

// prefix sum for occurences of each character
// for each query,

void solve() {
    int n, q;
    string a, b;
    cin >> n >> q >> a >> b;
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    unordered_map<char, vector<int>, custom_hash> ma;
    unordered_map<char, vector<int>, custom_hash> mb;

    for (char c : alpha) {
        ma[c] = vector<int>(1, 0);
        mb[c] = vector<int>(1, 0);

        for (char p : a) {
            if (p == c) {
                ma[c].push_back(end(ma[c])[-1] + 1);
            } else {
                ma[c].push_back(end(ma[c])[-1]);
            }
        }

        for (char p : b) {
            if (p == c) {
                mb[c].push_back(end(mb[c])[-1] + 1);
            } else {
                mb[c].push_back(end(mb[c])[-1]);
            }
        }
    }

    for (size_t i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        l--;
        int diff = 0;

        for (auto &[c, v] : ma) {
            diff += abs(v[r] - v[l] - mb[c][r] + mb[c][l]);
        }
        cout << diff / 2 << "\n";
    }
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