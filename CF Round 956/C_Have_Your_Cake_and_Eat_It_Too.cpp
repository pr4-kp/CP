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

vector<int> valid(vector<int> order, vector<vector<ll>> ps, ll goal) {
    int n = ps[0].size() - 1;
    int l1 = 0, r1 = 0;
    int l2 = 0, r2 = 0;
    int l3 = 0, r3 = 0;

    for (int i = 0; i < n; ++i) {
        if (ps[order[0]][i + 1] >= goal) {
            r1 = i;
            l2 = i + 1;
            r2 = i + 1;
            break;
        }
    }
    if (r2 == 0) {
        return {-1};
    }

    for (int i = l2; i < n; ++i) {
        if (ps[order[1]][i + 1] - ps[order[1]][l2] >= goal) {
            r2 = i;
            l3 = i + 1;
            r3 = i + 1;
            break;
        }
    }
    if (r3 == 0) {
        return {-1};
    }

    if (ps[order[2]][n] - ps[order[2]][r2 + 1] >= goal) {
        r3 = n - 1;
        return {l1 + 1, r1 + 1, l2 + 1, r2 + 1, l3 + 1, r3 + 1};
    } else return {-1};
}

void solve() {
    int n;
    cin >> n;
    vector<vector<ll>> a(3, vector<ll>(n, 0));
    vector<vector<ll>> ps(3, vector<ll>(n + 1, 0));

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
            ps[i][j + 1] += ps[i][j] + a[i][j];
        }
    }

    ll goal = ((end(ps[0]))[-1] + 2) / 3;
    vector<vector<int>> perms = {{0, 1, 2},
                                 {0, 2, 1},
                                 {1, 0, 2},
                                 {1, 2, 0},
                                 {2, 0, 1},
                                 {2, 1, 0}};
    for (int i = 0; i < 6; ++i) {
        auto a = valid(perms[i], ps, goal);
        if (a.size() != 1) {
            for (int j = 0; j < 3; ++j) {
                if (perms[i][j] == 0) {
                    cout << a[j * 2] << " " << a[j * 2 + 1] << " ";
                }
            }
            for (int j = 0; j < 3; ++j) {
                if (perms[i][j] == 1) {
                    cout << a[j * 2] << " " << a[j * 2 + 1] << " ";
                }
            }
            for (int j = 0; j < 3; ++j) {
                if (perms[i][j] == 2) {
                    cout << a[j * 2] << " " << a[j * 2 + 1] << " ";
                }
            }
            cout << "\n";
            return;
        }
    }
    cout << "-1\n";
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