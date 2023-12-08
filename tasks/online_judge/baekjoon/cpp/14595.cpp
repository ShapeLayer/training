#include <bits/stdc++.h>
#define MAX 1'000'000
using namespace std;

int parents[MAX];

inline int find(int n) {
  if (n == parents[n]) return n;
  return parents[n] = find(parents[n]);
}

inline void merge(int a, int b) {
  int pa = find(a), pb = find(b);
  if (pa > pb) {
    parents[pb] = pa;
    parents[b] = pa;
  } else {
    parents[pa] = pb;
    parents[a] = pb;
  }
}

int main () {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n, m;
  cin >> n >> m;
  int a, b;
  for (int i = 0; i < n + 1; i++) parents[i] = i;
  vector<pair<int, int>> vec;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    vec.push_back(make_pair(a, b));
  }
  sort(vec.begin(), vec.end());
  int latest = 0;
  for (int i = 0; i < vec.size(); i++) {
    int a = vec[i].first;
    int b = vec[i].second;
    a = max(a, latest);
    for (int i = a; i < b + 1; i++) merge(a, i);
    latest = max(latest, b);
  }
  int count = 1, prev = find(1);
  for (int i = 2; i < n + 1; i++) {
    int now = find(i);
    if (now != prev) count++;
    prev = now;
  }
  cout << count << endl;
  return 0;
}
