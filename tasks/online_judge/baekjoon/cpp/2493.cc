#include "bits/stdc++.h"
using namespace std;

int main() {
  int N;
  cin >> N;

  int recv[N], tower[N];
  memset(recv, 0, N * sizeof(int));

  for (int i = 0; i < N; i++) cin >> tower[i];

  // value, index
  deque<pair<int, int>> s;
  for (int i = N - 1; i >= 0; i--) {
    auto now = tower[i];

    while (s.size()) {
      auto __saved = s.back();
      if (__saved.first <= now) {
        recv[__saved.second] = i + 1;
        s.pop_back();
      } else {
        break;
      }
    }
    s.push_back(make_pair(now, i));
  }

  for (int i = 0; i < N; i++) {
    cout << recv[i] << ' ';
  }
  cout << endl;

  return 0;
}
