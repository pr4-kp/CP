#include <algorithm>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int r, c, n;
    cin >> r >> c >> n;
    int d = 0;

    vector<pair<int, int>> frontier, l;
    vector<vector<bool>> visited(r, vector<bool>(c));

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        l.push_back({x, y});
    }

    while (!frontier.empty()) {
        for (const auto &[x, y] : l) {
            cout << x << " " << y << endl;
        }
    }
}