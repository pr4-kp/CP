#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
using ll = long long;

void solve() {
    ll n,c;

    cin >> n >> c;

    vector<ll> a(n);
    vector<ll> psum(n + 1);

    for (int i=0; i<n; ++i) {
        cin >> a[i];
        psum[i+1] = psum[i] + a[i];
    }

    int mi = distance(a.begin(), max_element(a.begin(), a.end()));

    for (int i=0; i<n; ++i) { 
        if (i < mi) {
            if (psum[i+1] + c >= a[mi]) cout << i << " ";
            else cout << i+1 << " ";
        }
        else if (i == mi) {
            if (a[0] + c >= a[i]) cout << i << " ";
            else cout << 0 << " ";
        }
        else {
            cout << i << " ";
        }
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}