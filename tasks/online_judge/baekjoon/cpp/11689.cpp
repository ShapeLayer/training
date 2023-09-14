#include <bits/stdc++.h>
#define i64 long long
using namespace std;

/*
 * Euler phi function
 * phi(n) = n * (1 - 1 / p_1) * (1 - 1 / p_2) * ... * (1 - 1 / p_m)
 * 
 * conversion: euler_phi -= euler_phi / p_i
 * get p_i: use p when n % p == 0 and n /= p
 */

int main() {
  i64 n, euler_phi;
  cin >> n;
  euler_phi = n;
  for (i64 p = 2; p * p <= n; p++) {
    if (n % p == 0)
      euler_phi -= euler_phi / p;
    while (n % p == 0)
      n /= p;
  }
  if (n > 1) euler_phi -= euler_phi / n;
  cout << euler_phi << endl;
  return 0;
}
