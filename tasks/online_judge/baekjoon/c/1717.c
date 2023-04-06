#include <stdio.h>

int parents[1000001];

int find(int n) {
  if (parents[n] == n) return n;
  int y = find(parents[n]);
  parents[n] = y;
  return y;
}

void merge(int a, int b) {
  int pa = find(a), pb = find(b);
  if (pa > pb) parents[pa] = pb;
  else if (pa < pb) parents[pb] = pa;
}

int main() {
  int n, m;
  for (int i = 1; i < 1000001; i++) parents[i] = i;
  scanf("%d %d", &n, &m);
  for (int i = 0; i < m; i++) {
    int o, a, b;
    scanf("%d %d %d", &o, &a, &b);
    if (o == 0) merge(a, b);
    else {
      if (find(a) == find(b)) printf("YES\n");
      else printf("NO\n");
    }
  }
}