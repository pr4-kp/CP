#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

ll MOD = 1'000'000'007;

int main()
{
    int n;
    cin >> n;
    vector<string> board(n);

    for (int i=0;i<n;i++) {
        cin >> board[i];
    }

    vector<vector<ll> > dp(n, vector<ll>(n,0));
    dp[0][0]=1;

    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (board[i][j] == '*') dp[i][j] = 0;
            else {
                if (i > 0)
                    dp[i][j] += dp[i - 1][j] % MOD;
                if (j > 0)
                    dp[i][j] += dp[i][j - 1] % MOD;
            }
        }
    }
    cout << end(end(dp)[-1])[-1] % MOD << endl;
}