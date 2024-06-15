#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
using ll = long long;

void solution() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i=0;i<n;++i) {
        cin >> a[i];
    }

    ll val = 1'000'000'001;

    for (ll i=0;i<n-1;++i) {
        val = min(val,max(a[i], a[i+1]));
    }

    cout << val-1 << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t; while(t--) { 
        solution();
    }
}