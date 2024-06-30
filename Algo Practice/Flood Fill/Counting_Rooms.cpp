#include<algorithm>
#include<vector>
#include<tuple>
#include<iostream>
#include<queue>
#include<ranges>

using namespace std;
namespace R = std::ranges;
namespace V = std::ranges::views;

void floodFill(int n, int m, vector<vector<bool>>& visited, vector<string>& grid, tuple<int, int> start)
{
    queue<tuple<int, int>> q;
    visited[get<0>(start)][get<1>(start)] = true;
    q.push(start);

    while (!q.empty())
    {
        auto pos = q.front();
        q.pop();

        if (get<0>(pos) + 1 < n && grid[get<0>(pos) + 1][get<1>(pos)] == '.' 
                && !visited[get<0>(pos) + 1][get<1>(pos)])
        {
            q.push({get<0>(pos) + 1, get<1>(pos)});
            visited[get<0>(pos) + 1][get<1>(pos)] = true;
        }

        if (get<0>(pos) - 1 >= 0 && grid[get<0>(pos) - 1][get<1>(pos)] == '.' 
                && !visited[get<0>(pos) - 1][get<1>(pos)])
        {
            q.push({get<0>(pos) - 1, get<1>(pos)});
            visited[get<0>(pos) - 1][get<1>(pos)] = true;
        }

        if (get<1>(pos) + 1 < m && grid[get<0>(pos)][get<1>(pos) + 1] == '.' 
                && !visited[get<0>(pos)][get<1>(pos) + 1])
        {
            q.push({get<0>(pos), get<1>(pos) + 1});
            visited[get<0>(pos)][get<1>(pos) + 1] = true;
        }

        if (get<1>(pos) - 1 >= 0 && grid[get<0>(pos)][get<1>(pos) - 1] == '.' 
                && !visited[get<0>(pos)][get<1>(pos) - 1])
        {
            q.push({get<0>(pos), get<1>(pos) - 1});
            visited[get<0>(pos)][get<1>(pos) - 1] = true;
        }
    }
}

int main()
{
    int n,m;
    cin >> n >> m;

    auto visited = vector<vector<bool>>(n, vector<bool>(m));
    auto grid = vector<string>(n);

    for (int i = 0; i<n; ++i) {
        cin >> grid[i];
    }

    int ans = 0;

    for (auto y : V::iota(0,n))
    {
        for (int x : V::iota(0,m))
        {
            if (grid[y][x] == '.' && !visited[y][x])
            {
                floodFill(n, m, visited, grid, {y, x});
                ans += 1;
            }
        }
    }

    cout << ans << endl;
}