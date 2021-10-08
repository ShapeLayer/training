#include <iostream>
using namespace std;

int primes[10001];
int main(void) {
  for (int i = 2; i < 10001; i++) primes[i] = 1;
  for (int i = 0; i < 10001; i++) {
    if (primes[i]) {
      for (int j = 1; j*i < 10001; j++) {
        primes[j*i] = 0;
      }
    }
  }
  int m, n, min = 0, sum = 0, exists = 0;
  cin >> m >> n;
  for (int i = m; m <= n; i++) {
    if (primes[i]) {
      exists = 1;
      if (min == 0) min = i;
      sum += i;
    }
  }
  if (!exists) cout << -1;
  else cout << sum << endl << min << endl;
  return 0;
}