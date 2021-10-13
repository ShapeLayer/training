#include <iostream>
using namespace std;

bool primes[10000001];
int main(void) {
  for (int i = 2; i < 10000001; i++) primes[i] = true;
  for (int i = 2; i < 10000001; i++) {
    if (primes[i]) {
      for (int j = 2; i*j < 10000001; j++) primes[i*j] = false;
    }
  }
  int n;
  cin >> n;
  for (int i = 2; i < 10000001; i++) {
    if (primes[i]) {
      while (n % i == 0) {
        cout << i << endl;
        n /= i;
      }
    }
  }
  return 0;
}