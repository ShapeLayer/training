#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;

  int ones = 0, twos = 0;
  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    if (a == 1) ++ones;
    else ++twos;
  }

  cout << (ones >= twos && (ones - twos) % 3 == 0 ? "Yes" : "No") << '\n';
}
