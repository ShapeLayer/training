#include "bits/stdc++.h"
#define u64 unsigned long long
using namespace std;

int main() {
  u64 n;
  cin >> n;
  int zero_end = -1;
  for (int i = 0; i < 64; i++) {
    if (zero_end == -1) {
      if (n & 1 << i) {
        zero_end = i;
      };
    }
  }
  cout << 64 - zero_end << endl;
}
