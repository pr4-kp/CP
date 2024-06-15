#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;

    vector<ll> dp(n+1, INT32_MAX);
    dp[n] = 0;

    for (int i=n; i > 0; --i) {
        string s = to_string(i);
        for (char &c : s) {
            int cv = c - '0';
            if (i - cv >= 0) {
                dp[i - cv] = min(dp[i - cv], dp[i] + 1);
            }
        }
    }

    cout << dp[0];
}

