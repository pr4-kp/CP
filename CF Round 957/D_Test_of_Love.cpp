#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <string>
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
    int n, m, k;
    cin >> n >> m >> k;
    string a;
    cin >> a;

    a = "L" + a + "L";

    vector<int> dp(n + 2, n + 10); // dp stores the minimum amount of swimming to get to position i
    dp[0] = 0;

    for (int i = 1; i < n + 2; ++i) {
        if (a[i] == 'C') {
            continue;
        } else {
            bool seen_croc = false;
            for (int j = i - 1; j >= max(0, i - m); --j) {
                if (a[j] == 'L') {
                    dp[i] = min(dp[i], dp[j]);
                } else if (a[j] == 'W' && !seen_croc) {
                    dp[i] = min(dp[i], dp[j] + (i - j));
                } else {
                    seen_croc = true;
                }
            }
        }
    }
    if (end(dp)[-1] <= k) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
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