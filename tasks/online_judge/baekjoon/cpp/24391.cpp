#include <bits/stdc++.h>
#define MAX 100'000
using namespace std;

int parents[MAX];

int find(int n) {
  if (parents[n] == n) return n;
  return parents[n] = find(parents[n]);
}

void merge(int a, int b) {
  int pa = find(a), pb = find(b);
  if (pa > pb) {
    parents[pa] = pb;
    parents[a] = pb;
  } else {
    parents[pb] = pa;
    parents[b] = pa;
  }
}

int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n + 1; i++) parents[i] = i;
  int a, b;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    merge(a, b);
  }
  int count = 0;
  int prev, now;
  cin >> prev;
  for (int i = 1; i < n; i++) {
    cin >> now;
    if (find(prev) != find(now)) count++;
    prev = now;
  }
  cout << count << endl;
  return 0;
}
