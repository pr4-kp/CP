#include <algorithm>
#include <chrono>
#include <iostream>
#include <stack>
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

// Function to return required minimum sum
int sumSubarrayMins(int A[], int n) {
    int left[n], right[n];

    stack<pair<int, int>> s1, s2;

    // getting number of element strictly larger
    // than A[i] on Left.
    for (int i = 0; i < n; ++i) {
        int cnt = 1;

        // get elements from stack until element
        // greater than A[i] found
        while (!s1.empty() && (s1.top().first) > A[i]) {
            cnt += s1.top().second;
            s1.pop();
        }

        s1.push({A[i], cnt});
        left[i] = cnt;
    }

    // getting number of element larger than A[i] on Right.
    for (int i = n - 1; i >= 0; --i) {
        int cnt = 1;

        // get elements from stack until element greater
        // or equal to A[i] found
        while (!s2.empty() && (s2.top().first) >= A[i]) {
            cnt += s2.top().second;
            s2.pop();
        }

        s2.push({A[i], cnt});
        right[i] = cnt;
    }

    int result = 0;

    // calculating required resultult
    for (int i = 0; i < n; ++i)
        result = (result + A[i] * left[i] * right[i]);

    return result;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int A[3] = {1, 2, 3};
    cout << sumSubarrayMins(A, 3) << "\n";
}