#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main()
{
    int n, x;

    cin >> n >> x;

    vector<int> prices(n);
    vector<int> pages(n);

    for (int i = 0; i < n; ++i)
    {
        cin >> prices[i];
    }
    for (int i = 0; i < n; ++i)
    {
        cin >> pages[i];
    }

    vector<vector<int> > dp(n,vector<int>(x+1));

    for (int j=prices[0];j<x+1;++j) {
        dp[0][j] = pages[0];
    }

    for (int i=1;i<n;++i) {
        for (int j=0; j<x+1;++j) {
            // computing the most pages we can get with at most j dollars by getting (subset of) the first i books

            if (j - prices[i] >= 0) 
                dp[i][j] = max(dp[i][j], dp[i-1][j-prices[i]] + pages[i]);

            dp[i][j] = max(dp[i][j], dp[i - 1][j]);
        }
    }

    cout << end(end(dp)[-1])[-1];
}