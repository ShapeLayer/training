#include <bits/stdc++.h>
#define MAX (int)1e10
using namespace std;

int n, costs[16][16] = {0, }, dp[16][1 << 16] = {0, };

void step(int curr, int prev, int bits) {
  if (bits == (1 << n) - 1) {
    if (dp[curr][0] == 0) return MAX;
  }
  int mask = 1 << curr;
  dp[curr][bits | mask] = min(dp[curr][bits | mask], dp[prev][bits] + costs[prev][curr]);
  cout << dp[prev][bits] << ' ' << costs[prev][curr] << endl;
  for (int i = 0; i < n; i++) {
    if ((bits | mask) & (1 << i) != (1 << i)) {
      step(i, curr, bits | mask);
    }
  }
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    dp[i][0] = 0;
    for (int j = 1; j < 1 << 16; j++)
      dp[i][j] = MAX;
    for (int j = 0; j < n; j++)
      cin >> costs[i][j];
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (i != j)
        step(i, j, 1 << j);
    }
  }

  int result = MAX;
  for (int i = 0; i < n; i++) {
    cout << 'r' << ' ' <<  i << ' ' << dp[i][(1 << n) - 1];
    result = min(result, dp[i][(1 << n) - 1]);
  }
  cout << result << endl;

  return 0;
}
