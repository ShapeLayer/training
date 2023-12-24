#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    char gets[99];
    int count = 0, res = 0;
    for (int a = 0; a < n; a++) {
        cin >> gets;
        count = 0;
        for (int i = 0; i < m; i++) {
            if (gets[i] == 'O') count++;
        }
        if (count > m / 2) res++;
    }
    
    cout << res << '\n';
    return 0;
}