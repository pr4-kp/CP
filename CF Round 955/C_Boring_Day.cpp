#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

void solve() {
    ll n, l, r;
    cin >> n >> l >> r;
    vector<ll> a(n);
    for (ll i = 0; i < n; ++i) {
        cin >> a[i];
    }

    ll ans = 0;
    ll running = 0;
    ll lp = 0;
    ll rp = 0;

    while (rp <= n) {
        // cout << lp << " " << rp << endl;
        if (l <= running && running <= r) {
            ans += 1;
            running = 0;
            lp = rp;
            rp = rp;
        } else if (running < l) {
            running += a[rp];
            rp += 1;
        } else if (running > r) {
            running -= a[lp];
            lp += 1;
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