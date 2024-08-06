/**
 * Idea: sqrt decomposition
 * For each query, if k < R = sqrt(N), then we can just precompute it in O(RN) = O(N sqrt(N))
 * If k > R, then the level can grow to at most sqrt(N), so we can perform prefix sums + binary search to
 * compute when level ups happen and what we are at for the ith monster
 * This takes O(R*R*log(N)) = O(N log(N)).
 * Each query for the second case will take O(N/R log(N)) = O(Rlog(N)). So in total, its O(q*sqrt(N)log(N)).
 *
 * sqrt(N) = sqrt(200000) is too small and will cause the k>R
 * precomputation to take up too much memory, choose slightly higher and take advantage of a bitset
 */

#include <algorithm>
#include <bitset>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

const int N = 200200;
const int R = 2000;
const int M = N / R + 5;

bitset<N + 1> small_q[R + 1];

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, q;
    cin >> n >> q;
    vector<int> monster_level(n);
    for (int i = 0; i < n; i++) {
        cin >> monster_level[i];
    }

    // if k <= R, precompute if we can kill the monster at position i by simulating it
    for (int i = 1; i <= R; i++) {
        int level = 1;
        int killed = 0;

        for (int j = 1; j <= n; j++) {
            if (monster_level[j - 1] >= level) {
                small_q[i][j - 1] = 1;
                killed++;
            }
            if (killed >= i) {
                level++;
                killed = 0;
            }
        }
    }

    // killable_monsters[r][i] stores the number of monsters up to (and including i)
    // that have level greater than or equal to r
    vector<int> killable_monsters[M + 1];
    for (int r = 1; r <= M; r++) {
        killable_monsters[r] = vector<int>(n + 1, 0);

        for (int j = 0; j < n; j++) {
            if (monster_level[j] >= r) {
                killable_monsters[r][j + 1] = killable_monsters[r][j] + 1;
            } else {
                killable_monsters[r][j + 1] = killable_monsters[r][j];
            }
        }
    }

    // begin queries
    while (q--) {
        int i, x;
        cin >> i >> x;
        i--;

        if (x <= R) { // use the precomputations
            if (small_q[x][i])
                cout << "YES\n";
            else
                cout << "NO\n";
        } else {
            // binary search on the prefix sum for x to find what level
            // you are at position i
            int level_at_i = 1; // current level
            int level_up = 0;   // the position where you level up (+1)

            while (true) {
                auto level_up_time = lower_bound(killable_monsters[level_at_i].begin() + (level_up + 1),
                                                 killable_monsters[level_at_i].end(),
                                                 killable_monsters[level_at_i][level_up] + x);

                if (level_up_time == killable_monsters[level_at_i].end()) {
                    break;
                } else {
                    level_up = level_up_time - killable_monsters[level_at_i].begin();
                    if (level_up - 1 < i) {
                        level_at_i++;
                    } else {
                        break;
                    }
                }
            }

            if (monster_level[i] >= level_at_i)
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }
}
