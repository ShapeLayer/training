#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n, h, gets;
  cin >> n >> h;
  int b2t[h + 1], t2b[h + 1];
  for (int i = 0; i < h + 1; i++) {
    b2t[i] = 0;
    t2b[i] = 0;
  }
  for (int i = 0; i < n; i++) {
    cin >> gets;
    if (i % 2 == 0) b2t[gets]++;
    else t2b[h - gets + 1]++;
  }
  for (int i = 1; i < h + 1; i++) {
    b2t[h - i] += b2t[h - i + 1];
    t2b[i] += t2b[i - 1];
  }
  int _min = (int)1e8, count = 0;
  for (int i = 1; i < h + 1; i++) {
    int now = b2t[i] + t2b[i];
    if (now < _min) {
      _min = now;
      count = 1;
    } else if (now == _min) count++;
  }
  cout << _min << ' ' << count << endl;
  return 0;
}
