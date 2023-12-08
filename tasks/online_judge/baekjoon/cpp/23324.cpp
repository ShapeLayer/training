#include <bits/stdc++.h>
#define i64 int64_t
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
    parents[pb] = pa;
    parents[b] = pa;
  } else {
    parents[pa] = pb;
    parents[a] = pb;
  }
}

int main() {
  int n, m, k, uk, vk;
  cin >> n >> m >> k;
  for (int i = 0; i < n + 1; i++) parents[i] = i;
  int a, b;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    if (i == k - 1) uk = a, vk = b;
    else merge(a, b);
  }
  i64 cnt_uk = 0, cnt_vk = 0;
  uk = find(uk), vk = find(vk);
  for (int i = 1; i < n + 1; i++) {
    int p = find(i);
    if (p == uk) cnt_uk++;
    else if (p == vk) cnt_vk++;
  }
  cout << cnt_uk * cnt_vk << endl;
  return 0;
}
