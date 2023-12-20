#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <bits/stdc++.h>
#define MAX (int)1e4

using namespace std;

int n, gets[MAX + 2], req = 0;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  cin >> n;
  for (int i = 0; i < n; i++) cin >> gets[i];
  gets[n] = 0, gets[n + 1] = 0;

  int able;
  for (int i = 0; i < n; i++) {
    if (gets[i + 1] > gets[i + 2]) {
      /*
       * 4
       * 1 2 1 1
       * 의 경우 첫번째-두번째를 먼저 지우고 다음으로 넘기도록 함
       */
      able = min(gets[i], gets[i + 1] - gets[i + 2]);
      req += able * 5;
      gets[i] -= able;
      gets[i + 1] -= able;
      able = min(gets[i], min(gets[i + 1], gets[i + 2]));
      req += able * 7;
      gets[i] -= able;
      gets[i + 1] -= able;
      gets[i + 2] -= able;
    } else {
      /*
       * 4
       * 1 3 3 1
       * 의 경우 첫번째-두번째-세번째를 모두 지우고
       * 첫번째-두번째를 처리하면 됨
       */
      able = min(gets[i], min(gets[i + 1], gets[i + 2]));
      req += able * 7;
      gets[i] -= able;
      gets[i + 1] -= able;
      gets[i + 2] -= able;
      able = min(gets[i], gets[i + 1]);
      req += able * 5;
      gets[i] -= able;
      gets[i + 1] -= able;
    }
    req += gets[i] * 3;
  }

  cout << req << '\n';
  return 0;
}
