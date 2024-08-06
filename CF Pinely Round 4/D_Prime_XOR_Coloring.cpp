/**
 * a^b = p
 * <==> a^b^b = p^b
 * <==> a = p^b
 * <==> p^a = p^p^b
 * <==> p^a = b
 *
 * so compute all primes (O(nlogn))
 * connect a to p^a
 *
 */

#include <algorithm>
#include <chrono>
#include <iostream>
#include <queue>
#include <stdint.h>
#include <unordered_set>
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

    if (n == 1) {
        cout << "1\n1\n";
    } else if (n == 2) {
        cout << "2\n1 2\n";
    } else if (n == 3) {
        cout << "2\n1 2 2\n";
    } else if (n == 4) {
        cout << "3\n1 2 2 3\n";
    } else if (n == 5) {
        cout << "3\n1 2 2 3 3\n";
    } else if (n == 6) {
        cout << "4\n1 2 2 3 3 4\n";
    } else {
        cout << "4\n";
        for (size_t i = 0; i < n; i++) {
            cout << (i % 4) + 1 << " ";
        }
        cout << "\n";
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