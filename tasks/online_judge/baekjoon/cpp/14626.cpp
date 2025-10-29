#include "bits/stdc++.h"
using namespace std;

int main() {
  char isbn[14];
  cin >> isbn;

  int offset = 1;
  int nan_offset = -1;
  int sum_for_validation = 0;
  for (int i = 0; i < 13; i++) {
    if ('0' <= isbn[i] && isbn[i] <= '9') {
      sum_for_validation += ((int)isbn[i] - 48) * offset;
    } else {
      nan_offset = offset;
    }
    offset = (offset + 2) % 4;
  }

  int result = 0;
  for (int i = 0; i < 10; i++) {
    if ((sum_for_validation + i * nan_offset) % 10 == 0) {
      result = i;
      break;
    }
  }
  cout << result << endl;

  return 0;
}
