#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

class MaxSegTree
{

private:
    ll len;

    vector<ll> segtree;

public:
    MaxSegTree(ll len) : len(len), segtree(2 * len) {}

    void set(ll ind, ll val)
    {

        for (segtree[ind += len] = val; ind > 1; ind >>= 1)
        {

            segtree[ind >> 1] = max(segtree[ind], segtree[ind ^ 1]);
        }
    }

    // maximum of the range [from, to)

    ll range_max(ll from, ll to)
    {

        ll max_ = INT32_MIN;

        for (from += len, to += len; from < to; from >>= 1, to >>= 1)
        {

            if ((from & 1) != 0)
            {
                max_ = max(max_, segtree[from++]);
            }

            if ((to & 1) != 0)
            {
                max_ = max(max_, segtree[--to]);
            }
        }

        return max_;
    }
};

int main()
{
    int n;
    cin >> n;
    vector<ll> x(n);
    MaxSegTree stx(n);
    vector<ll> dp(n,1);

    for(int i=0;i<n;i++){
        cin >> x[i];
        stx.set(i, x[i]);
    }

    for(int i=0;i<n;++i) {
        stx.range_max(0, i-1)
        for (int j=i-1; j>=0; --j) {
            if (x[j] < x[i])
                dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    cout << *max_element(dp.begin(), dp.end()) << endl;
}