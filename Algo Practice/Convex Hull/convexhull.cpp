#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <vector>

using namespace std;
using ll = long long;

static uint64_t x;

uint64_t next() {
    uint64_t z = (x += 0x9e3779b97f4a7c15);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9;
    z = (z ^ (z >> 27)) * 0x94d049bb133111eb;
    return z ^ (z >> 31);
}
/**
 * Use with
 * unordered_map<long long, int, custom_hash> safe_map;
 * gp_hash_table<long long, int, custom_hash> safe_hash_table;
 * so you don't get hacked :(
 */
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

struct Point {
    int x, y;
    Point(int a = 0, int b = 0) : x(a), y(b) {}
    bool operator<=>(const Point &) const = default;
    Point operator-(const Point &a) {
        return Point(x - a.x, y - a.y);
    }
    friend istream &operator>>(istream &in, Point &p) {
        int x, y;
        in >> p.x >> p.y;
        return in;
    }
};

vector<int> convexHull(const vector<Point> &v) {
    int ind = distance(v.begin(), min_element(v.begin(), v.end()));
    vector<int> cand, C{ind};
    for (int i = 0; i < v.size(); ++i)
        if (v[i] != v[ind])
            cand.push_back(i);

    sort(cand.begin(), cand.end(), [&](int a, int b) {
        Point x = v[a] - v[ind], y = v[b] - v[ind];
    });
}

void solve(int n) {
    vector<Point> vp(n);

    for (int i = 0; i < n; ++i) {
        cin >> vp[i];
    }

    vector<int> out = convexHull(vp);

    cout << out.size() << endl;
    for (int v : out) {
        cout << vp[v].x << " " << vp[v].y << endl;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t != 0) {
        solve(t);
        cin >> t;
    }
}