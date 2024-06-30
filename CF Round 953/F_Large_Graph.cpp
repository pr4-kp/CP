#include <algorithm>
#include <chrono>
#include <iostream>
#include <map>
#include <stdint.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
using ll = long long;

// https://usaco.guide/gold/dsu
class DisjointSets {

  public:
    vector<int> parents;
    vector<int> sizes;

    DisjointSets(int size) : parents(size), sizes(size, 1) {
        for (int i = 0; i < size; i++) {
            parents[i] = i;
        }
    }

    /** @return the "representative" node in x's component */
    int find(int x) {
        return parents[x] == x ? x : (parents[x] = find(parents[x]));
    }

    /** @return whether the merge changed connectivity */
    bool unite(int x, int y) {
        int x_root = find(x);

        int y_root = find(y);

        if (x_root == y_root) {
            return false;
        }

        if (sizes[x_root] < sizes[y_root]) {
            swap(x_root, y_root);
        }

        sizes[x_root] += sizes[y_root];

        parents[y_root] = x_root;

        return true;
    }

    /** @return whether x and y are in the same connected component */
    bool connected(int x, int y) { return find(x) == find(y); }
};

// https://codeforces.com/blog/entry/62393
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

vector<vector<int>> sieve(int n) {
    vector<vector<int>> prime_factors(n + 1, vector<int>(0));
    for (int i = 2; i < n + 1; ++i) {
        if (prime_factors[i].empty()) {      // i.e. if i is prime
            for (int k = i; k < n; k += i) { // everything multiplied by i also has i as a prime factor
                prime_factors[k].push_back(i);
            }
        }
    }
    return prime_factors;
}

auto pf = sieve(1e6 + 5); // precompute the values

void solve() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int> solve(2 * n - 1);

    for (int i = 1; i < n; ++i) {
        solve[i - 1] = a[i];
    }
    for (int i = 0; i < n; ++i) {
        solve[i + n - 1] = a[i];
    }

    DisjointSets dsu(2 * n - 1);

    unordered_map<int, int, custom_hash> lp; // last primes

    for (int i = 0; i < 2 * n - 1; ++i) {
        for (int f : pf[solve[i]]) { // iterate over the factors of e
            if (lp.contains(f) && abs(lp[f] - i) <= k) {
                dsu.unite(lp[f], i);
            }
            lp[f] = i;
        }
    }

    unordered_set<int, custom_hash> u;
    for (auto e : dsu.parents) {
        u.insert(dsu.find(e));
    }
    ll ans = u.size();

    for (int i = 0; i < n; ++i) {
        if (a[i] == 1) {
            if (i == 0) ans += n - 1;
            else ans += n - 2;
        }
    }

    cout << ans << endl;
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