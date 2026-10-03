#include "bits/stdc++.h"
#define i64 long long int
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  i64 A[N];
  i64 oper = 0;
  for (int i = 0; i < N; i++) cin >> A[i];

  if (K > 0) {
    for (int i = 1; i < N; i++) {
      if (A[i] <= A[i - 1]) {
        i64 __op2 = (A[i - 1] - A[i]) / abs(K) + 1;
        oper += __op2;
        A[i] += __op2 * K;
      }
    }
  } else {
    for (int i = N - 2; i >= 0; i--) {
      if (A[i] >= A[i + 1]) {
        i64 __op2 = (A[i] - A[i + 1]) / abs(K) + 1;
        oper += __op2;
        A[i] += __op2 * K;
      }
    }
  }
  
  cout << oper << endl;

  return 0;
}
