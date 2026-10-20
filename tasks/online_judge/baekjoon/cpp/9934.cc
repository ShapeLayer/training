#include "bits/stdc++.h"
#define IDX(y, x) (1 << y) + x
#define ENDL '\n'
using namespace std;

void visit(int *tree, queue<int> *q, int N, int y, int x) {
  int idx = IDX(y, x);
  
  if (y + 1 < N) {
    visit(tree, q, N, y + 1, x * 2);
  }

  tree[idx] = q->front();
  q->pop();
  if (y + 1 < N) {
    visit(tree, q, N, y + 1, x * 2 + 1);
  }
}

int main() {
  int N, buf;
  cin >> N;

  int tree[1 << N];
  for (int i = 0; i < (1 << N); i++) tree[i] = 0;
  
  // (1 << i) + j (for j in 0..2<<i)
  queue<int> q;
  for (int i = 0; i < (1 << N) - 1; i++) {
    cin >> buf;
    q.push(buf);
  }

  visit(tree, &q, N, 0, 0);

  for (int y = 0; y < N; y++) {
    for (int x = 0; x < (1 << y); x++) {
      cout << tree[IDX(y, x)] << ' ';
    }
    cout << ENDL;
  }

  return 0;
}
