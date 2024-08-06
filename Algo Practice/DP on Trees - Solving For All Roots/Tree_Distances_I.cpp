#include <algorithm>
#include <cassert>
#include <chrono>
#include <iostream>
#include <queue>
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

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<unordered_set<int>> g(n, unordered_set<int>());
    vector<unordered_set<int>> dir_g(n, unordered_set<int>());
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].insert(v);
        g[v].insert(u);
    }

    vector<int> first(n, 0);
    vector<int> second(n, 0);
    vector<int> ans(n, 0);

    queue<int> bfs;
    vector<bool> visited(n, false);
    vector<int> order;
    bfs.push(0);

    while (!bfs.empty()) {
        int node = bfs.front();
        order.push_back(node);
        bfs.pop();
        visited[node] = true;

        for (auto i : g[node]) {
            if (!visited[i]) {
                dir_g[node].insert(i);
                bfs.push(i);
            }
        }
    }

    debug(order);
    assert(order.size() == n);

    for (int i = n - 1; i >= 0; i--) {
        int node = order[i];
        for (auto ch : dir_g[node]) {
            if (first[ch] + 1 > first[node]) {
                second[node] = first[node];
                first[node] = first[ch] + 1;
            } else if (first[ch] + 1 > second[node]) {
                second[node] = first[ch] + 1;
            }
        }
    }

    ans[0] = first[0];

    debug(first, second);

    for (int i = 0; i < n; i++) {
        int node = order[i];
        for (auto ch : dir_g[node]) {
            debug(node, ch, ans[i]);
            if (first[ch] + 1 == first[node]) {
                ans[ch] = max({second[node] + 1, ans[node] + 1});
            } else {
                ans[ch] = max({first[node] + 1, ans[node] + 1});
            }
        }
    }

    // debug(first, second, ans);

    for (auto e : ans) {
        cout << e << " ";
    }
    cout << "\n";
}