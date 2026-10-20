#include "bits/stdc++.h"
#define ABS(N) (N < 0 ? -N : N)
#define ENDL '\n'
using namespace std;

int main() {
  priority_queue<pair<int, int>> pq;
  int N;
  int oper;

  cin >> N;

  for (int _ = 0; _ < N; _++) {
    cin >> oper;
    if (!oper) {
      if (pq.size() == 0) {
        cout << 0 << ENDL;
      } else {
        cout << -pq.top().second << ENDL;
        pq.pop();
      }
    } else {
      pq.push(make_pair(-ABS(oper), -oper));
    }
  }
  return 0;
}
