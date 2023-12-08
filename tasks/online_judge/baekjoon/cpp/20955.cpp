#include <bits/stdc++.h>
#define MAX 100'000
using namespace std;

int parents[MAX];

int find(int n) {
  if (n == parents[n]) return n;
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
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n, m, u, v;
  cin >> n >> m;
  int opers = 0;
  for (int i = 0; i < n + 1; i++) parents[i] = i;
  for (int i = 0; i < m; i++) {
    cin >> u >> v;
    if (find(u) == find(v)) opers++;
    else merge(u, v);
  }
  set<int> s = { 1 };
  int prev = find(1), now;
  for (int i = 2; i < n + 1; i++) {
    now = find(i);
    if (prev != now) s.insert(now);
  }
  cout << opers + s.size() - 1 << endl;
  return 0;
}
