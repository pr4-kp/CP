/**
 * We need the preliminary check: (1) that the arrays actually contain the same elements
 * The only invariant between the arrays is the parity between them, so check if a is odd/even and b is odd/even
 * If there are duplicates, then we can mess with the parity anyway, so the answers is always YES is that case
 * otherwise, the answer is YES if a.parity == b.parity and NO otherwise
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
    vector<int> a(n);
    vector<int> b(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    auto acpy = a;
    auto bcpy = b;

    sort(acpy.begin(), acpy.end());
    sort(bcpy.begin(), bcpy.end());
    for (int i = 0; i < n; ++i) {
        if (acpy[i] != bcpy[i]) {
            cout << "NO\n";
            return;
        }
    }

    for (int i = 1; i < n; ++i) {
        if (acpy[i] == acpy[i - 1]) {
            cout << "YES\n";
            return;
        }
    }

    unordered_map<int, int, custom_hash> r; // reassign values (coordinate compression?)
    for (int i = 0; i < n; ++i) {
        r[a[i]] = i;
    }
    for (int i = 0; i < n; ++i) {
        b[i] = r[b[i]];
        // cout << b[i] << " ";
    }
    // cout << endl;

    vector<bool> visited(n, false);
    int parity = 0;
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            int cyc = 1;
            visited[i] = true;
            int trav = b[i];
            while (!visited[trav]) {
                visited[trav] = true;
                trav = b[trav];
                cyc++;
            }
            // cout << cyc << " ";
            parity += (cyc - 1);
        }
    }
    // cout << endl;
    // cout << parity << "\n";

    if (parity % 2 == 1) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
    }

    // cout << "MAYBE\n";
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