#include "bits/stdc++.h"
using namespace std;

int main() {
  int32_t n;
  cin >> n;

  int32_t m = ~n + 1;

  int count = 0;
  for (int i = 0; i < 32; i++) {
    if ((n & 1) ^ (m & 1)) {
      count++;
    }
    n >>= 1;
    m >>= 1;
  }

  cout << count << endl;

  return 0;
}
