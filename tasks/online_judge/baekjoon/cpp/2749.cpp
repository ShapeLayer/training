#include <bits/stdc++.h>
#define i64 long long
#define mod 1'000'000
using namespace std;

int get_cycle() {
  int a = 1, b = 1, count = 0;
  while (true) {
    int calc = (a + b) % mod;
    a = b;
    b = calc;
    count++;
    if (a == b && a == 1) break;
  }
  return count;
}

int main() {
  i64 n;
  int p = get_cycle();
  int fibo[p] = {0, 1, 1, };
  cin >> n;
  for (int i = 2; i < p; i++) {
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % mod;
  }
  cout << fibo[n % p] << endl;
  return 0;
}
