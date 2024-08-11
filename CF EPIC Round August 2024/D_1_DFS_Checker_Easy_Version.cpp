#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <unordered_set>
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
Query in O(n):
- iterate through the permutation
- if any element is visited before its parent in the original tree, print NO
- if all elements are good, print YES

Obs. It suffices to store the smallest index of all the children of each node in the permutation

Swap operation:
Obs. We need to change first_index[] sometimes
1. If the node is first_index of something and it moves, first_index of the parent turns to the new position
    - the parent may become invalid
    can check

Obs. Whatever it swaps, we need to check if the one that goes up becomes valid, or the one the goes down because invalid
1. Swap up becomes valid if it becmoes less than its first child
2. Swap down becomes invalid if it becomes more than its first child
*/

const int MAX = 3e5 + 10;

void solve() {
    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    vector<int> parent(n, -1);
    for (int i = 1; i < n; i++) {
        cin >> parent[i];
        parent[i]--;
    }
    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        p[i]--;
    }

    vector<int> first_index(n, MAX);
    bitset<MAX> valid;
    int good = 0;

    for (int i = 0; i < n; ++i) {
        if (parent[p[i]] == -1) continue;
        first_index[parent[p[i]]] = min(first_index[parent[p[i]]], i);
    }
    for (int i = 0; i < n; ++i) {
        if (first_index[p[i]] > i) {
            valid[i] = 1;
            good++;
        }
    }

    debug(parent);
    debug(p);
    debug(first_index);
    for (int i = 0; i < n; ++i) {
        cerr << valid[i] << " ";
    }
    cerr << "\n";

    for (int i = 0; i < q; ++i) {
        int x, y;
        cin >> x >> y;
        x--, y--;

        swap(p[x], p[y]);

        if (x <= first_index[p[y]] && parent[p[x]] == p[y]) {
            first_index[p[y]] = x;
            if (valid[y]) {
                good--;
            }
            valid[y] = false;
        }
        if (y <= first_index[p[x]] && parent[p[y]] == p[x]) {
            first_index[p[x]] = y;
            if (valid[x]) {
                good--;
            }
            valid[x] = false;
        }
        if (y < first_index[p[y]]) {
            if (!valid[y]) {
                good++;
            }
            valid[y] = true;
        } else {
            if (valid[y]) {
                good--;
            }
            valid[y] = false;
        }
        if (x < first_index[p[x]]) {
            if (!valid[x]) {
                good++;
            }
            valid[x] = true;
        } else {
            if (valid[x]) {
                good--;
            }
            valid[x] = false;
        }

        debug(first_index);
        for (int i = 0; i < n; ++i) {
            cerr << valid[i] << " ";
        }
        cerr << "\n";
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