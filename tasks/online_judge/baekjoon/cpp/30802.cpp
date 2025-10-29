#include "bits/stdc++.h"
using namespace std;

#define C(T, E) ((E / T) + ((E % T != 0) ? 1 : 0))

int main() {
  int N, S, M, L, XL, XXL, XXXL, T, P;
  cin >> N >> S >> M >> L >> XL >> XXL >> XXXL >> T >> P;

  cout << C(T, S) + C(T, M) + C(T, L) + C(T, XL) + C(T, XXL) + C(T, XXXL) << endl;
  cout << N / P << ' ' << N % P << endl;
}
