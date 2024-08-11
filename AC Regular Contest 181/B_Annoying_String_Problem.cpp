#include <algorithm>
#include <chrono>
#include <iostream>
#include <stdint.h>
#include <string>
#include <vector>

#ifndef ONLINE_JUDGE
#include "template.cpp"
#else
#define debug(...)
#define debugArr(...)
#endif

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

// https://stackoverflow.com/questions/6021274/finding-shortest-repeating-cycle-in-word
string findSmallestUnit(string str) {
    vector<int> lps(str.length(), 0);
    int i = 1;
    int len = 0;

    while (i < str.length()) {
        if (str[i] == str[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len == 0) i++;
            else {
                len = lps[len - 1];
            }
        }
    }
    int n = str.length();
    int x = lps[n - 1];
    if (n % (n - x) == 0) {
        return str.substr(0, n - x);
    }
    return str;
}

void solve() {
    string s, x, y;
    cin >> s >> x >> y;

    // simple checks: set S=T
    if (x.size() == y.size()) {
        cout << "Yes\n";
        return;
    }

    // set S=0
    int count_zero[] = {0, 0};

    for (auto c : x) {
        if (c == '0') {
            count_zero[0]++;
        }
    }

    for (auto c : y) {
        if (c == '0') {
            count_zero[1]++;
        }
    }

    if (count_zero[0] == count_zero[1]) {
        cout << "Yes\n";
        return;
    }

    cout << "Maybe\n";

    cout << findSmallestUnit(s) << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--)
        solve();
}