#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n, m, a, b, count = 0;
    cin >> n >> m;
    a = b = 1;
    // cycle: 1, 1, ..., 0
    while (true) {
      int calc = (a + b) % m;
      a = b;
      b = calc;
      count++;
      if (a == b && a == 1) break;
    }
    cout << n << ' ' << count << endl;
  }
  return 0;
}
