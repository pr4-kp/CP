#include <vector>
#include <algorithm>
#include <iostream>
#include <ranges>

using namespace std;
namespace R = ranges; 
namespace V = ranges::views;

const int MAXN = 2000000;

vector <int> prime;
bool is_composite[MAXN];

void linear_sieve (int n) {
    fill (is_composite, is_composite + n, false);
    // for (int i=2;i<n;++i) {
    for (auto i : V::iota(2,n)) {
        if (!is_composite[i]) prime.push_back(i);
        for (size_t j = 0; j < prime.size () && i*prime[j]<n; ++j) {
            is_composite[i * prime[j]] = true;
            if (i%prime[j]==0) break;
        }
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    linear_sieve(MAXN);
    long out = 0;
    for (long i = 2; i < MAXN; i++) {
        if (!is_composite[i]) out += i;
    }

    cout << out << endl;
    cout << prime[10000] << endl;
}
