#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <bits/stdc++.h>
#define i64 __int64_t
#define MAX (int)1e6

using namespace std;

i64 n, b, c, gets[MAX + 2], req = 0;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  cin >> n;
  b = 3, c = 2;
  i64 _1 = b, _2 = b + c, _3 = b + 2 * c;
  for (int i = 0; i < n; i++) cin >> gets[i];
  gets[n] = 0, gets[n + 1] = 0;

  i64 able;
  for (int i = 0; i < n; i++) {
    if (gets[i + 1] > gets[i + 2]) {
      able = min(gets[i], gets[i + 1] - gets[i + 2]);
      req += able * _2;
      gets[i] -= able;
      gets[i + 1] -= able;
      able = min(gets[i], min(gets[i + 1], gets[i + 2]));
      req += able * _3;
      gets[i] -= able;
      gets[i + 1] -= able;
      gets[i + 2] -= able;
    } else {
      able = min(gets[i], min(gets[i + 1], gets[i + 2]));
      req += able * _3;
      gets[i] -= able;
      gets[i + 1] -= able;
      gets[i + 2] -= able;
      able = min(gets[i], gets[i + 1]);
      req += able * _2;
      gets[i] -= able;
      gets[i + 1] -= able;
    }
    req += gets[i] * _1;
  }

  cout << req << '\n';
  return 0;
}
