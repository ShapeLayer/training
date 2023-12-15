#include <bits/stdc++.h>
#define MAX (int)1e10
#define MIN -1
#define MOD 1999
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n;
  int min_a[32][2], min_b[32][2];
  int max_a[32][2], max_b[32][2];
  int arr_a[32], arr_b[32];
  int cnt_a[32], cnt_b[32];

  for (int i = 0; i < 32; i++) {
    for (int j = 0; j < 2; j++) {
      min_a[i][j] = MAX;
      min_b[i][j] = MAX;
      max_a[i][j] = MIN;
      max_b[i][j] = MIN;
    }
    cnt_a[i] = 0;
    cnt_b[i] = 0;
  }
  cin >> n;
  for (int i = 0; i < n; i++) cin >> arr_a[i];
  for (int i = 0; i < n; i++) cin >> arr_b[i];

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 32; j++) {
      if (arr_a[i] & (1 << j)) {
        cnt_a[j] += 1;
        min_a[j][1] = min(arr_a[i] & ((1 << (j + 1)) - 1), min_a[j][1]);
        max_a[j][1] = max(arr_a[i] & ((1 << (j + 1)) - 1), max_a[j][1]);
      } else {
        min_a[j][0] = min(arr_a[i] & ((1 << (j + 1)) - 1), min_a[j][0]);
        max_a[j][0] = max(arr_a[i] & ((1 << (j + 1)) - 1), max_a[j][0]);
      }
      if (arr_b[i] & 1 << j) {
        cnt_b[j] += 1;
        min_b[j][1] = min(arr_b[i] & ((1 << (j + 1)) - 1), min_b[j][1]);
        max_b[j][1] = max(arr_b[i] & ((1 << (j + 1)) - 1), max_b[j][1]);
      } else {
        min_b[j][0] = min(arr_b[i] & ((1 << (j + 1)) - 1), min_b[j][0]);
        max_b[j][0] = max(arr_b[i] & ((1 << (j + 1)) - 1), max_b[j][0]);
      }
    }
  }


  int res_1 = 0;
  for (int i = 0; i < 32; i++) {
    res_1 = (res_1 + 1 * cnt_a[i] % MOD * cnt_b[i] % MOD * (1 << i)) % MOD;
  }
    
  int arr[32];
  for (int i = 0; i < 32; i++) {
    arr[i] = 1;
  }

  int p = 1;
  for (int i = 0; i < 32; i++) {
    if (min_a[i][0] != MAX && min_b[i][0] != MAX && ((min_a[i][0] + min_b[i][0]) & p) == 0) {
      arr[i] = 0;
    }
    if (min_a[i][1] != MAX && min_b[i][1] != MAX && ((min_a[i][1] + min_b[i][1]) & p) == 0) {
      arr[i] = 0;
    }
    if (max_a[i][1] != MIN && max_b[i][0] != MIN && ((max_a[i][1] + max_b[i][0]) & p) == 0) {
      arr[i] = 0;
    }
    if (max_a[i][0] != MIN && max_b[i][1] != MIN && ((max_a[i][0] + max_b[i][1]) & p) == 0) {
      arr[i] = 0;
    }
    p <<= 1;
  }

  int res_2 = 0;
  int cache = 1;
  for (int i = 0; i < 32; i++) {
    if (arr[i] != 0) {
      res_2 += cache;
    }
    cache <<= 1;
  }

  cout << res_1 << ' ' << res_2 << endl;
  return 0;
}
