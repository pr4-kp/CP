#include <algorithm>
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

    int operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<unordered_set<int, custom_hash>> g(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;

        g[u].insert(v);
        g[v].insert(u);
    }

    // check if graph is bipartite
    bool is_bipartite = true;
    queue<int> bfs;
    vector<int> color(n, -1);

    bfs.push(0);
    color[0] = 0;

    while (!bfs.empty()) {
        int start = bfs.front();
        bfs.pop();

        for (auto e : g[start]) {
            if (color[e] == -1) {
                color[e] = !color[start];
                bfs.push(e);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (auto adj : g[i]) {
            if (adj != i && color[adj] == color[i]) {
                is_bipartite = false;
            }
        }
    }

    debug(n, m);
    debug(is_bipartite);

    vector<int>
        color_set[2];

    for (int i = 0; i < n; i++) {
        if (color[i] == 0)
            color_set[0].push_back(i);
        else if (color[i] == 1)
            color_set[1].push_back(i);
    }
    int k = color_set[0].size(), l = color_set[1].size();

    if (is_bipartite) { // if the graph is bipartite, chose Bob and try to color as bipartite
        cout << "Bob\n";
        cout.flush();

        // color everything with 0 -> 1
        // color everything with 1 -> 2
        // if we finish coloring one of these, find 3 or other color to fill in the other one
        int k_done = 0, l_done = 0;

        int c1, c2;
        for (int i = 0; i < n; i++) {
            cin >> c1 >> c2;

            if (k_done < k && l_done < l) {
                if (c1 == 1 || c2 == 1) {
                    cout << color_set[0][k_done] + 1 << " 1\n";
                    cout.flush();
                    k_done++;
                } else {
                    cout << color_set[1][l_done] + 1 << " 2\n";
                    cout.flush();
                    l_done++;
                }
            } else if (k_done == k) {
                int oth;

                if (c1 != 1)
                    oth = c1;
                else
                    oth = c2;

                cout << color_set[1][l_done] + 1 << " " << oth << "\n";
                cout.flush();
                l_done++;
            } else {
                int oth;

                if (c1 != 2)
                    oth = c1;
                else
                    oth = c2;

                cout << color_set[0][k_done] + 1 << " " << oth << "\n";
                cout.flush();
                k_done++;
            }
        }
    } else { // if the graph is not bipartite, pick Alice and then choose 1 2 for n turns
        cout << "Alice\n";
        cout.flush();

        int in1, in2;
        for (int i = 0; i < n; i++) {
            cout << "1 2\n";
            cout.flush();
            cin >> in1 >> in2;
        }
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