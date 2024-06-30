#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

void solve() {
    ll x, y, k;
    cin >> x >> y >> k;

    while (k > 0) {
        if (x < y) {
            x -= 1;
            x = (x + k) % (y - 1);
            x += 1;
            x %= y;
            break;
        }

        if (x % y != 0) {
            ll rem = min(k, y - (x % y));
            x += rem;
            k -= rem;
            while (x % y == 0) {
                x /= y;
            }
        } else {
            x += 1;
            while (x % y == 0) {
                x /= y;
            }
            k--;
        }
    }

    cout << x << endl;
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