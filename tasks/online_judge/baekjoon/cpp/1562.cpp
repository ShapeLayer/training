#include <bits/stdc++.h>
#define i64 long long
#define MOD 1'000'000'000
using namespace std;

int n;

int main() {
  cin >> n;
  
  // dp[len][latest][bit]: 계단수의 개수
  int dp[n + 1][10][1 << 10] = {0, };
  for (int i = 1; i < 10; i++) {
    dp[1][i][1 << i] = 1;
  }

  for (int i = 2; i < n + 1; i++) {
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 1 << 10; k++) {
        int buf = 0, bit = k | (1 << j);
        if (j != 0) 
          buf = dp[i - 1][j - 1][k];
        if (j != 9)
          buf = (buf + dp[i - 1][j + 1][k]) % MOD;
        dp[i][j][bit] = (dp[i][j][bit] + buf) % MOD;
      }
    }
  }
  
  int res = 0 ;
  for (int i = 0; i < 10; i++) {
  /*
   * (notice) cpp 연산자 결합 순위
   * 4: +-
   * 5: << >>
   * 1 << 10 - 1 하면 512가 나온다
   */
    res = (res + dp[n][i][(1 << 10) - 1]) % MOD;
  }
  cout << res << endl;
  return 0;
}
