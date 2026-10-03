#include "bits/stdc++.h"
#define i64 long long int
using namespace std;

int main() {
  int N, D;
  cin >> N >> D;
  int X[N];
  for (int i = 0; i < N; i++) { cin >> X[i]; }

  sort(X, X + N);

  i64 range = 0;
  i64 left = 0, right = 0;
  i64 base = left = right = X[0] - D;
  
  if (D == 0) {
    cout << '0' << endl;
    return 0;
  }

  for (int i = 0; i < N; i++) {
    left = X[i] - D;
    if (left > right) {
      range -= left - right;
    }
    right = X[i] + D;
  }
  range += X[N - 1] + D - base;

  cout << range << endl;

  return 0;
}
