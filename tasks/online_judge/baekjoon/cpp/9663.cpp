#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
#include <bits/stdc++.h>

using namespace std;

int res = 0, line[15], n;

inline bool check(int each) {
  for (int i = 0; i < each; i++) {
    if (line[each] == line[i]) return false;
    if (abs(line[each] - line[i]) == each - i) return false;
  }
  return true;
}

inline void step(int each) {
  if (each == n) res++;
  else {
    for (int i = 0; i < n; i++) {
      line[each] = i;
      if (check(each)) step(each + 1);
    }
  }
}

int main() {
	ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  cin >> n;
  step(0);
  cout << res << '\n';
  return 0;
}