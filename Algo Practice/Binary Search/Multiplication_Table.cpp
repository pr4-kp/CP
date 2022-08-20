#include <iostream>
#include <cmath>
using namespace std;

long long calc_less_than(long long mid, long long n);

int main() {
    long long n;
    cin >> n;
    
    if (n == 1) {
        cout << 1;
    } 

    else {
        long long left = 0, right = n * n, mid;

        while (left < right) {
            mid = left + (right - left) / 2;

            if (calc_less_than(mid, n) >= ((n * n + 1) / 2)) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }
        cout << right << endl;
    }
    
    return 0;
}

long long calc_less_than(long long mid, long long n) {
    long long ans = 0;
    for (long long row = 1; row <= n; row++) {
        // cout << "added " << mid / row << endl;
        ans += min(mid / row, n);
    }
    return ans;
}