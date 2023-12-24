#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    long long count = (2 * n + 1) * (2 * n + 1);
    for (int i = 0; i < 2 + n; i++) {
        if (i == n) continue;
        count += ((1 + n) - i) + 1;
    }
    cout << count << '\n';
    return 0;
}