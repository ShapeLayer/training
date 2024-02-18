#include "bits/stdc++.h"
using namespace std;

int n;
int p, x;
int main() {
  cin >> n;
  vector<pair<int, int>> v;
  int prev_x = -1, counts = 0;
  int total = 0;
  for (int i = 0; i < n; i++) {
    cin >> x >> p;
    if (i == 0) {
      prev_x = x;
    } else {
      total += (x - prev_x) * counts;
    }
    total += p;
    counts++;
    prev_x = x;
    v.push_back(make_pair(x, p));
  }
  sort(v.begin(), v.end());
  int max_opt = max(
    (v[1].first - v[0].first) * (n - 1) + v[0].second,
    (v[n - 1].first - v[n - 2].first) * (n - 1) + v[n - 1].second
  );
  
  for (int i = 1; i < n; i++) {
    max_opt = max(
      max_opt,
      (v[i].first - v[i - 1].first) * (n - i) + v[i - 1].second
    );
    // cout << (v[i].first - v[i - 1].first) * (n - i + 1) + v[i - 1].second << '\n';
  }

  cout << total - max_opt << '\n';
  return 0;
}