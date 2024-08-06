/**
 * Observations:
 * Alice takes things greedily
 * If Alice took n moves and just took the ith cake, then Bob can "distribute" n moves
 * however he wants amongst the remaining cakes
 */

#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <unordered_map>
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
    unordered_map<int, int, custom_hash> ord;
    vector<int> cts(n, 0);

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int v = 0;
    ord[a[0]] = v;
    cts[v]++;

    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) {
            v++;
            ord[a[i]] = v;
            cts[v]++;
        } else {
            cts[v]++;
        }
    }

    // the number of different cakes
    int m = ord.size();

    // [i][j] <-> the maximum remaining moves if Bob let Alice take exactly j of the first i cakes
    // initialize everything to negative except (0, 0); negative means this state is impossible
    vector<vector<ll>> bobMoves(m + 1, vector<ll>(m + 1, -1));
    bobMoves[0][0] = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j <= i; j++) {
            if (bobMoves[i][j] >= 0) {
                // if Bob lets Alice take the next cake, then he gains 1 more move
                // this event is now possible because we assign it a positive number
                bobMoves[i + 1][j + 1] = max(bobMoves[i + 1][j + 1], bobMoves[i][j] + 1);
                // if Bob can take the current cake from Alice, then he loses cts[i] moves
                if (bobMoves[i][j] >= cts[i]) {
                    bobMoves[i + 1][j] = max(bobMoves[i + 1][j], bobMoves[i][j] - cts[i]);
                }
            }
        }
    }

    ll out = m;
    for (int i = 0; i < m + 1; ++i) {
        if (bobMoves[m][i] >= 0) {
            out = i;
            break;
        }
    }
    cout << out << endl;
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