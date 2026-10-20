#include "bits/stdc++.h"
using namespace std;

int main() {
  int N;
  cin >> N;
  string oper;
  deque<int> q;
  int operand;
  for (int _ = 0; _ < N; _++) {
    cin >> oper;
    if (oper == "push") {
      cin >> operand;
      q.push_back(operand);
    } else if (oper == "pop") {
      if (q.size() == 0) {
        cout << -1 << endl;
        continue;
      }
      cout << q.front() << endl;
      q.pop_front();
    } else if (oper == "size") {
      cout << q.size() << endl;
    } else if (oper == "empty") {
      cout << (q.size() == 0 ? 1 : 0) << endl;
    } else if (oper == "front") {
      cout << (q.size() > 0 ? q.front() : -1) << endl;
    } else if (oper == "back") {
      cout << (q.size() > 0 ? q.back() : -1) << endl;
    }
  }
  return 0;
}
