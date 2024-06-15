#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool solution()
{
    long n;
    cin >> n;

    vector<long> a(n);
    vector<long> b(n);

    for (long i=0; i < n; ++i) {
        cin >> a[i];
    }
    for (long i = 0; i < n; ++i) {
        cin >> b[i];
    }

    long m;
    cin >> m;

    vector<long> d(m);

    for (long i=0; i<m; ++i) {
        cin >> d[i];
    }

    map<long, long> diffs;
    map<long, long> dmap;

    for (long i=0;i<n;++i) {
        if (a[i] != b[i]) {
            if (!diffs.contains(b[i]))
                diffs.insert({b[i], 0});
            diffs[b[i]] += 1;
        }
    }

    for (long i = 0; i < m; ++i) {
        if (!dmap.contains(d[i]))
            dmap.insert({d[i], 0});
        dmap[d[i]] += 1;
    }
    
    
    if (find(b.begin(), b.end(), d[m - 1]) == b.end()) return false;

    // check that the diffs of b[] are a sub(multi)set of d[]
    for (const auto &p : diffs) {
        if (!dmap.contains(p.first) || p.second > dmap[p.first])
            return false;
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long t;
    cin >> t;

    while(t--){
        cout << (solution() ? "YES" : "NO") << endl;
    }
}