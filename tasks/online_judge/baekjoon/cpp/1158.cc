#include "bits/stdc++.h"
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;
  deque<int> q;
  for (int i = 0; i < N; i++) q.push_back(i + 1);

  deque<int> result;
  int cnt = 0;
  while (q.size()) {
    for (int i = 0; i < K; i++) {
      auto now = q.front();
      q.pop_front();
      if (++cnt % K == 0) {
        result.push_back(now);
      } else {
        q.push_back(now);
      }
    }
  }
  cout << '<';
  for (int i = 0; i < N - 1; i++) {
    cout << result.front() << ',' << ' ';
    result.pop_front();
  }
  cout << result.front();
  cout << '>' << endl;
  return 0;
}
