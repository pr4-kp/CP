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

static tuple<int, int, int> THREE[] = {
    {0, 1, 2},
    {0, 1, 3},
    {0, 2, 3},
    {1, 2, 3},
    {0, 1, 4},
    {0, 2, 4},
    {1, 2, 4},
    {0, 3, 4},
    {1, 3, 4},
    {2, 3, 4}};

static tuple<int, int, int> OTHER[] = {
    {3, 4, 5},
    {2, 4, 5},
    {1, 4, 5},
    {0, 4, 5},
    {2, 3, 5},
    {1, 3, 5},
    {0, 3, 5},
    {1, 2, 5},
    {0, 2, 5},
    {0, 1, 5},
};

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

void solve(int n, vector<ll> a) {
    int l, r;
    cin >> l >> r;
    int m = r - l + 1;
    if (m >= 48) {
        // if there are at least 48 sticks in the interval, a triangle can be formed by the problem bounds
        cout << "YES\n";
    } else {
        r--;
        l--;

        vector<ll> as(a.begin() + l, a.begin() + (r + 1));
        int first_ind = m;
        int last_ind = -1;
        sort(begin(as), end(as));

        // for (auto e : as) {
        //     cout << e << " ";
        // }
        // cout << "\n";

        for (int i = 0; i < m - 2; i++) {
            if (as[i] + as[i + 1] > as[i + 2]) {
                first_ind = min(first_ind, i);
                last_ind = max(last_ind, i);
            }
        }

        if (first_ind != -1 && last_ind - first_ind >= 3) {
            cout << "YES\n";
            return;
        }

        for (int i = 0; i < m - 5; ++i) {
            for (int j = 0; j < 10; ++j) {
                const auto &[x, y, z] = THREE[j];
                const auto &[x2, y2, z2] = OTHER[j];

                ll first[3] = {as[i + x], as[i + y], as[i + z]};
                ll second[3] = {as[i + x2], as[i + y2], as[i + z2]};

                if (first[0] + first[1] > first[2] && second[0] + second[1] > second[2]) {
                    cout << "YES\n";
                    return;
                }
            }
        }

        // if passes none, there is no triple
        cout << "NO\n";
        return;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, q;
    cin >> n >> q;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    while (q--) {
        solve(n, a);
    }
}