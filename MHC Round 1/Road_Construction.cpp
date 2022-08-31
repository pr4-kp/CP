#include<iostream>
#include<vector>

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<int> parents, size;
    for (int i = 0; i <= n + 1; i++) {
        parents.push_back(i);
        size.push_back(1);
    }

    return 0;
}