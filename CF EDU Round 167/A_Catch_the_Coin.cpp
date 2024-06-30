#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    while (n--) {
        int x, y;
        cin >> x >> y;

        if (y >= -1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}