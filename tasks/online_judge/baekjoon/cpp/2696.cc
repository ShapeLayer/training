#include "bits/stdc++.h"
#define ENDL '\n'
using namespace std;

int get_mid(priority_queue<int> *);

int main() {
  int T, N;
  int buf;
  bool is_odd = false;
  
  cin >> T;
  for (int _ = 0; _ < T; _++) {
    cin >> N;
    is_odd = false;
    priority_queue<int> pq;
    cout << N / 2 + 1 << ENDL;
    for (int i = 0; i < N; i++) {
      is_odd = !is_odd;
      cin >> buf;
      pq.push(buf);
      if (is_odd) {
        cout << get_mid(&pq) << ' ';
      }
    }
    cout << ENDL;
  }

  return 0;
}

int get_mid(priority_queue<int> *pq) {
  int res;
  stack<int> buf;
  int init_size = pq->size();
  while (pq->size() > init_size / 2) {
    buf.push(pq->top());
    pq->pop();
  }
  res = buf.top();
  while (buf.size()) {
    pq->push(buf.top());
    buf.pop();
  }
  return res;
}
