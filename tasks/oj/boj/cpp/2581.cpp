#include <iostream>
using namespace std;

bool primes[10001];
int main(void) {
  for (int i = 2; i < 10001; i++) primes[i] = true;
  for (int i = 2; i < 10001; i++) {
    if (primes[i]) {
      for (int j = 2; j*i < 10001; j++) {
        primes[j*i] = false;
      }
    }
  }
  int m, n, min = 0, sum = 0; bool exists = 0;
  cin >> m >> n;
  for (int i = m; i <= n; i++) {
    if (primes[i]) {
      exists = true;
      if (min == 0) min = i;
      sum += i;
    }
  }
  if (!exists) cout << -1;
  else cout << sum << endl << min << endl;
  return 0;
}