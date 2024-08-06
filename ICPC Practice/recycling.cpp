#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <vector>

using namespace std;
using ll = long long;

template <class T>
struct RMQ {
    vector<vector<T>> jmp;
    RMQ(const vector<T> &V) : jmp(1, V) {
        for (int pw = 1, k = 1; pw * 2 <= sz(V); pw *= 2, ++k) {
            jmp.emplace_back(sz(V) - pw * 2 + 1);
            rep(j, 0, sz(jmp[k]))
                jmp[k][j] = min(jmp[k - 1][j], jmp[k - 1][j + pw]);
        }
    }
    T query(int a, int b) {
        assert(a < b); // or return inf if a == b
        int dep = 31 - __builtin_clz(b - a);
        return min(jmp[dep][a], jmp[dep][b - (1 << dep)]);
    }
};

struct sol {
    int left;
    int right;
    ll val;
};

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<ll> v(n);

    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    RMQ rmq(v);

    int l = 0;
    int r = n;

    sol out(0, n, n * rmq.query(0, n));

    while (l < r) {
        if (out.val < (r - l) * rmq.query(l, r)) {
            out = sol(l, r, (r - l) * rmq.query(l, r));
        } else if (out.val < ((r - 1) - l) * rmq.query(l, r - 1)) {
            r--;
            out = sol(l, r, (r - l) * rmq.query(l, r));
        } else if (out.val < (r - (l + 1)) * rmq.query(l + 1, r)) {
            l++;
            out = sol(l, r, (r - l) * rmq.query(l, r));
        }
    }
}