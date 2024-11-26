#include "bits/stdc++.h"
using namespace std;
struct edge {
  int from, to, cost;
} typedef edge_t;

bool compare(edge_t a, edge_t b) {
  return a.cost < b.cost;
}

int find(int parents[], int x) {
  if (parents[x] == x) {
    return x;
  }
  return parents[x] = find(parents, parents[x]);
}

void merge(int parents[], int a, int b) {
  int pa = find(parents, a);
  int pb = find(parents, b);
  if (a == b) {
    return;
  }
  if (pa < pb) {
    parents[pb] = pa;
    parents[b] = pa;
    return;
  } else {
    parents[pa] = pb;
    parents[a] = pb;
  }
}

int main() {
  int n, m, t;
  cin >> n >> m >> t;
  vector<edge_t> edges;
  for (int _ = 0; _ < m; _++) {
    int a, b, c;
    cin >> a >> b >> c;
    edge_t edge = {a, b, c};
    edges.push_back(edge);
  }
  sort(edges.begin(), edges.end(), compare);

  int parents[n + 1];
  for (int i = 0; i < n + 1; i++) {
    parents[i] = i;
  }

  int colony = 0;
  int result = 0;
  for (int i = 0; i < m; i++) {
    edge_t e = edges[i];
    int to = e.to, from = e.from, cost = e.cost;
    if (find(parents, from) == find(parents, to)) {
      continue;
    }
    merge(parents, from, to);
    result += cost + t * colony;
    colony++;
  }

  cout << result << endl;
  return 0;
}
