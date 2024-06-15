#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main() {
    int n,m;
    cin >> n >> m;

    vector<ll> visited(n);

    void dfs(int s) {
        if (visited[s])
            return;
        visited[s] = true;
        // process node s
        for (auto u : adj[s])
        {
            dfs(u);
        }
    }
}


